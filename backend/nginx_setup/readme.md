Description how to setup the nginx

In my case I used Linux Debian 

### First step: Install nginx, apache2-utils    
### Second step: create ```user``` with the password ```password_user```  

```bash
sudo htpasswd -c /etc/nginx/.htpasswd user
```
```-c``` we need to use only for the first user. All folowing users we can create with the following command  

```bash
sudo htpasswd /etc/nginx/.htpasswd another_user
```

If everything works fine the system will ask you to provide the password  

### Third step create the nginx config file
We gonna use the following [file](file_link.md)

### Forth step: close 9200 port for elasticsearch
ToDo!!!!

