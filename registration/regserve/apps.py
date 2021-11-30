from django.apps import AppConfig


class RegserveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'regserve'


#py manage.py makemigrations regserve
#py manage.py sqlmigrate regserve 0001
#py manage.py migrate