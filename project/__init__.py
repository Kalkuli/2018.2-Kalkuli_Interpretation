import os
from flask import Flask, jsonify
from project.api.views import interpret_blueprint


def create_app(script_info=None):

    app	= Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.register_blueprint(interpret_blueprint)
    return app
