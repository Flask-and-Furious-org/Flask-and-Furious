from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from App.database import create_db
from App.config import load_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    
    # Load config from your config file
    config = load_config()
    app.config.update(config)

    # Init DB + Login Manager
    db.init_app(app)
    login_manager.init_app(app)

    # Initialize DB schema
    create_db(app, db)

    # Import and register views/controllers
    from App.views import views
    for view in views:
        app.register_blueprint(view)

    from App.controllers.inventory_controller import inventory_views
    from App.controllers.recipe_controller    import recipe_views
        app.register_blueprint(inventory_views)
        app.register_blueprint(recipe_views)


    return app
