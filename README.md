# TOdolist APP

>2022/10/12

### 指令
- django-admin startproject todolist
- python manage.py runserver
- 新增app
    - python manage.py startaapp user

- setting.py[INSTALLED_APPS]
 - 'user.apps.UserConfig'

 - 進行資料庫同步
  -python manage.py migrate

- 新增超級管理者
    -python manage.py creayesuperuser
    -127.0.0.1:8000/admin
 - 語言跟時間變更
  -'zh-Hant'
  -'Asia/Taipei