# App/controllers/recipe_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_required
from App.models import db, Recipe, Ingredient

recipe_views = Blueprint("recipe_views", __name__, template_folder="../templates")

@recipe_views.route("/recipes")
@login_required
def recipes():
    return render_template("recipes.html", recipes=current_user.recipes)

@recipe_views.route("/recipes/new", methods=["GET", "POST"])
@login_required
def new_recipe():
    if request.method == "GET":
        return render_template("recipe_form.html", ingredients=current_user.ingredients)
    # POST
    title      = request.form["title"]
    directions = request.form["directions"]
    ids        = request.form.getlist("ingredient_ids")  # checkbox list
    rec = Recipe(title=title, directions=directions, owner=current_user)
    for ing_id in ids:
        rec.ingredients.append(Ingredient.query.get(int(ing_id)))
    db.session.add(rec)
    db.session.commit()
    return redirect(url_for("recipe_views.recipes"))

@recipe_views.route("/recipes/<int:rid>")
@login_required
def show_recipe(rid):
    rec = Recipe.query.get_or_404(rid)
    missing = rec.missing_items()
    return render_template("recipe_detail.html", r=rec, missing=missing)
