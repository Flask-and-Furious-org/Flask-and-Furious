from flask import Blueprint, render_template
from flask_login import login_required

home_views = Blueprint("home_views", __name__, template_folder="../templates")

@home_views.route("/")
@login_required               # redirect to /login if not authenticated
def dashboard():
    return render_template("index.html")
