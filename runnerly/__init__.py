import os
import logging
from flask import Flask

from runnerly.db.schema import db, User
from runnerly.blueprints.users import users as bp_users

logger = logging.getLogger(__name__)
blueprints = [bp_users]

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'runnerly.sqlite')}")

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    db.init_app(app)
    db.create_all(app=app)

    @app.route('/')
    def main():
        print(f'Config: {app.config}')
        return "OK, you got me now."

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
