#!/usr/bin/env python

# Example from:
# https://github.com/miguelgrinberg/REST-auth

import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

# to import custom libs
import imp

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_user_db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
user_db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class User(user_db.Model):
    __tablename__ = 'user'
    id = user_db.Column(user_db.Integer, primary_key=True)
    user_name = user_db.Column(user_db.String(256), index=True)
    user_email = user_db.Column(user_db.String(256), index=True)
    user_login = user_db.Column(user_db.String(32), index=True)
    user_password_hash = user_db.Column(user_db.String(64))

    def hash_user_password(self, user_password):
        self.user_password_hash = pwd_context.encrypt(user_password)

    def verify_user_password(self, user_password):
        return pwd_context.verify(user_password, self.user_password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user


@auth.verify_user_password
def verify_user_password(user_login_or_token, user_password):
    # first try to authenticate by token
    user = User.verify_auth_token(user_login_or_token)
    if not user:
        # try to authenticate with user_login/user_password
        user = User.query.filter_by(user_login=user_login_or_token).first()
        if not user or not user.verify_user_password(user_password):
            return False
    g.user = user
    return True


@app.route('/api/users', methods=['POST'])
def new_user():
    user_login = request.json.get('user_login')
    user_password = request.json.get('user_password')
    if user_login is None or user_password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(user_login=user_login).first() is not None:
        abort(400)    # existing user
    user = User(user_login=user_login)
    user.hash_user_password(user_password)
    user_db.session.add(user)
    user_db.session.commit()
    return (jsonify({'user_login': user.user_login}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})


@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'user_login': user.user_login})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.user_login})

if __name__ == '__main__':
    if not os.path.exists('user_db.sqlite'):
        user_db.create_all()
    app.run(debug=True)