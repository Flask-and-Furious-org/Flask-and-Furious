from App import create_app                     
from App.models import db, User, Ingredient

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    bob = User(username="bob", email="bob@example.com")
    bob.set_password("bobpass")
    db.session.add(bob)
    db.session.flush()           # so bob.id is available

    db.session.add(Ingredient(name="Flour", quantity="1 kg", owner=bob))
    db.session.add(Ingredient(name="Eggs",  quantity="4",    owner=bob))

    db.session.commit()
    print("🌱  Database seeded with demo user bob:bobpass")
