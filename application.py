# run.py
import os

from app import create_app as application

config_name = os.getenv('FLASK_CONFIG')
app = application(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)