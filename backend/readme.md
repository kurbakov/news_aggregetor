# Backend documentation

The backend I would split into 3 parts: 
- backend logic
- backend structure
- backend database

## Backend logic

The idea is very simple. lets imagine we have the databse with the list of the twitter accounts. For each account we have last twitter post id. So we can do incremental load to our database. The logic can be splitted into the following steps:
- Step 0: run create_db.py to create the database and populate twitter accounts.
- Step 1: get the list of twitter accounts from the database
- Step 2: send request to twitter to get the newests post
- Step 3: parse the twitter API reply
- Step 3: update the new last twitter post id in the database
- Step 4: run the analytical part (surrently it is the sentiment analysis for the news)
- Step 5: save news and information about the news source to the database
- Step 6: repete steps 1-5 each XX minutes

## Backend structure

The backend has the following components:
- Source code: Python 2.*
- Database: Elasticsearch
- Authorithation to the database and load balancer: Nginx
- API: Flask (currently we need only GET for the full text search)

The code consis of: 
- [classes/](https://github.com/kurbakov/project_a/tree/master/backend/classes): directory to store all classes that we gonna use in the project 
- [data/](https://github.com/kurbakov/project_a/tree/master/backend/data): directory to store any type of data. So for example we store labed twitter data (positive and negative tweets) so we can learn our classifier 
- [nginx_setup/](https://github.com/kurbakov/project_a/tree/master/backend/nginx_setup): description how to setup the nginx so people can recreate the project on their own hardware  
- [sentimetn_analysis/](https://github.com/kurbakov/project_a/tree/master/backend/sentimetn_analysis): classifier for the sentiment analysis 

As the execution files we have: 
- [create_db.py](https://github.com/kurbakov/project_a/blob/master/backend/create_db.py): file to create the data base and populate with temp data for development 
- [run_backend.py](https://github.com/kurbakov/project_a/blob/master/backend/run_backend.py): the main backend logic is here and this file should be later scheduled to run every XX minutes

## Backend database

The database is Elasticsearch. Has the following architecture:

### Index: twitter  
#### Document: twitter_data
{  
id: int8,  
news_text: text,  
twitter_page text,  
twitter_tag text,  
twitter_name text,  
news_created_at timestamp,  
latitude: float,  
longitude: float,  
positive_probability float,  
negative_probability float,  
}

#### Document: twitter_account
{  
id: int8,
twitter_name: text,  
twitter_tag: text,  
twitter_page: text,  
country text,  
city text,  
longitude float,  
latitude float,  
language float,  
max_twitter_id int8  
}

#### Index: user
#### Document: user_information
{  
id: int8,  
user_name: text,  
user_email: text,  
user_login: text,  
user_password: text  
}

For any questions please contact [Dmytro Kurbakov](https://github.com/kurbakov)
