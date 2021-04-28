import os

from app import application

config_name = 'development'
application = application(config_name)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=8080)