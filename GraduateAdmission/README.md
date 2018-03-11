# 清华大学工程物理系硕士研究生复试调剂信息填报系统

## 如何运行网站（开发模式）

```
# install dependencies
pip install django
pip install django-registration-redux
pip install pandas
pip install openpyxl
pip install reportlab
# setup database
python GraduateAdmission/manage.py migrate
# run server in development mode
python GraduateAdmission/manage.py runserver
```

## 如何部署
* collect static files
```
python GraduateAdmission/manage.py collectstatic
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
    server_name graduate-admission-server; 
    access_log /var/log/graduate_admission_access.log;
    error_log /var/log/graduate_admission_error.log;
    
    location = /favicon.ico {
        alias /path/to/favicon.ico;
    }
    location /static/ { 
        alias /path/to/staticfiles/; 
    } 
    location /media/ { 
        alias /path/to/media/; 
    } 
    location / { 
        proxy_pass http://unix:/tmp/graduate_admission.sock; 
    } 
}
```