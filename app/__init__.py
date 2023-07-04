from flask import Flask

from app.route import hello_world, index


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', index, methods=['GET', 'POST'])
    app.add_url_rule('/helloworld', '/helloworld', hello_world)
    return app
