from app import db

class Household(db.Model):
    id = db.Colum(db.Integer, primary_key=True, autoincrement=True)
    name = db.Coulum(db.Sting)
    members = db.relationship("User", secondary="group_members", backref="group")

