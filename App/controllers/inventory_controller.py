# App/controllers/inventory_controller.py
from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from flask_login import login_required, current_user
from App.models import db, Ingredient

inventory_views = Blueprint("inventory_views", __name__, template_folder="../templates")

@inventory_views.route("/pantry")
@login_required
def pantry():
    items = current_user.ingredients
    return render_template("pantry.html", items=items)

@inventory_views.route("/pantry", methods=["POST"])
@login_required
def add_item():
    name        = request.form["name"]
    quantity    = request.form.get("quantity", "")
    expiry_date = request.form.get("expiry_date")  # YYYY‑MM‑DD
    ing = Ingredient(name=name,
                     quantity=quantity,
                     expiry_date=expiry_date,
                     owner=current_user)
    db.session.add(ing)
    db.session.commit()
    return redirect(url_for("inventory_views.pantry"))

@inventory_views.route("/pantry/<int:item_id>/delete", methods=["POST"])
@login_required
def delete_item(item_id):
    Ingredient.query.filter_by(id=item_id, owner=current_user).delete()
    db.session.commit()
    return redirect(url_for("inventory_views.pantry"))
