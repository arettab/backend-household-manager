from app import db

class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
