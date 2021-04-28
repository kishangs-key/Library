# run.py
import os

from app import create_app as application

config_name = os.getenv('FLASK_CONFIG')
application = application(config_name)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=8080)