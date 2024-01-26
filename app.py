# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    x=10
    y=100
    z=2000000000
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'gfg'

    return app

def a():
    a()

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
