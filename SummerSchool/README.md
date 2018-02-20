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
```
pip install gunicorn
```