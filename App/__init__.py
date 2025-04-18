from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from App.database import create_db
from App.config    import load_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_url_path="/static")

    # ─── 1. Config  ─────────────────────────────────────────────
    config = load_config()
    app.config.update(config)

    # ─── 2. Extensions  ─────────────────────────────────────────
    db.init_app(app)
    login_manager.init_app(app)

    # ─── 3. Database schema  ───────────────────────────────────
    create_db(app, db)

    # ─── 4. Register legacy views (if you still need them) ─────
    from App.views import views            # dynamic list from original repo
    for view in views:
        app.register_blueprint(view)

    # ─── 5. Register Pantry Pal blueprints  ────────────────────
    from App.controllers.inventory_controller import inventory_views
    from App.controllers.recipe_controller    import recipe_views
    from App.controllers.home_controller      import home_views
    from App.controllers.auth                 import auth_views   # if you have one

    app.register_blueprint(auth_views)        # optional, keep if it exists
    app.register_blueprint(home_views)
    app.register_blueprint(inventory_views)
    app.register_blueprint(recipe_views)

    # ────────────────────────────────────────────────────────────
    return app
