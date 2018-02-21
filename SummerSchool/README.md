# 核学科夏令营网站

## 如何运行网站（开发模式）

```
# install dependency
pip install django
pip install django-registration-redux
# setup database
python SummerSchool/manage.py migrate
# run server in development mode
python SummerSchool/manage.py runserver
```

## 如何部署
* collect static files
```
python SummerSchool/manage.py collectstatic
```

* setup gunicorn
```
pip install gunicorn
./gunicorn_start
```

* deploy on nginx
```
# example conf
server {
    listen 80; 
    server_name summer-school-server; 
    access_log /var/log/summer_school_access.log;
    error_log /var/log/summer_school_error.log;
    
    location = /favicon.ico {
        alias /path/to/favicon.ico;
    }
    location /static/ { 
        alias /path/to/staticfiles/; 
    } 
    location / { 
        proxy_pass http://unix:/tmp/summer_school.sock; 
    } 
}
```