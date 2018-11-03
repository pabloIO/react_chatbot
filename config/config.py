from flask import Flask
import os

env = {
    'PORT'      : 3000,
    'HOST'      : '0.0.0.0',
    'IP'      : '192.168.0.101',
    'APP_ENV'   : 'DEV',
    'APP_SECRET': 'c3ds1bN@de',
    'APP'       : Flask(__name__, template_folder="public"),  
    'SQL_CONF'  : {
        'DB_NAME'  : 'users_comments',
        'DB_URI'   : str.format('sqlite:////{0}', os.path.abspath('database/users_comments.db'))
    },
    'NO_SQL_CONF':{
        'DB_NAME': 'reactbot',
        'DB_URI' : 'mongodb://localhost:27017',
    },
    'DELAY': 0.1
}
