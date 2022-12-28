import os
import secrets

from flask import Flask
from flask import render_template

from . import home_page

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    GENERATE_SECRET_KEY = secrets.token_urlsafe(16)

    app.config.from_mapping(
        SECRET_KEY=GENERATE_SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Registering blueprints
    app.register_blueprint(home_page.home_bp)

    return app