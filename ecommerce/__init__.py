# import pymysql

# pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopease_db',
        'USER': 'root',
        'PASSWORD': 'karthi@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}