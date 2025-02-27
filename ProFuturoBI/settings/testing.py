from .settings import *
DEBUG=True
#Crie a secret key para seu ambiente de teste
SECRET_KEY = 'django-insecure-ae+w)&yhn0x0a=lr(e52eu8$75ua8=m!+%6jjv1ijid(ppzrln'
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'default':{
    'ENGINE':'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
