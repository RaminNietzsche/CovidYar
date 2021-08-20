import os

from flask import Flask
import jinja2

from project.config import DefaultConfig as base_config

def create_app(config=None, app_name=base_config.DEFAULT_APP_NAME):
    app = Flask(app_name)

    # https://flask.palletsprojects.com/en/2.0.x/config/
    configure_app(app, config)

    # https://flask.palletsprojects.com/en/2.0.x/blueprints/
    configure_blueprints(app)

    # https://jinja.palletsprojects.com/en/3.0.x/api/
    configure_template(app)

    return app

def configure_app(app, config):
    if not config:
        config = base_config()
    app.config.from_object(config)

def configure_blueprints(app):
    for mod in app.config["MODULES"]:
        bp = __import__(f"project.apps.{mod}", fromlist=["views"])
        app.register_blueprint(bp.views.mod)

def configure_template(app):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = f"{base_dir}/{app.config['TEMPLATE_DIR']}/{app.config['TEMPLATE_NAME']}"
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([template_dir]),
    ])
    app.jinja_loader = my_loader