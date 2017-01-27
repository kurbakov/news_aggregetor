Description how to setup the nginx

In my case I used Linux Debian 

### 1 step: Install nginx, apache2-utils    
### 2 step: create ```user``` with the password ```password_user```  

```bash
sudo htpasswd -c /etc/nginx/.htpasswd user
```
```-c``` we need to use only for the first user. All folowing users we can create with the following command  

```bash
sudo htpasswd /etc/nginx/.htpasswd another_user
```

If everything works fine the system will ask you to provide the password  

### 3 step create the nginx config file
We gonna use the following [file](https://github.com/kurbakov/project_a/blob/master/backend/nginx_setup/nginx_custom.conf)

### 4 step: close 9200 port for elasticsearch
[ToDo!!!!](https://jamesmcfadden.co.uk/securing-elasticsearch-with-nginx)

### 5 step: run nginx
Now when we have the running elasticsearch we have to start the nginx
```bash
nginx -c /PATH/TO/nginx_custom.conf
```

Test that auth works fine:
```bash
curl -i user:password_user@127.0.0.1:8080
```
Should return 200 OK and 
```bash
curl -i 127.0.0.1:9200
```
Should return 401 ERROR

More information here:  
- [github: Example Nginx Configurations for Elasticsearch](https://gist.github.com/karmi/b0a9b4c111ed3023a52d)
- [elastic: Playing HTTP Tricks with Nginx](https://www.elastic.co/blog/playing-http-tricks-nginx)
- [digitalocean: How To Set Up Password Authentication with Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-nginx-on-ubuntu-14-04)
