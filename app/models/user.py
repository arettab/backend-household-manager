from typing import Self
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hoh = db.Column(db.Boolean, nullable=False)


    @classmethod
    def to_dict(cls, self):
        return dict(
            id=self.id,
            name=self.name,
            email=self.email,
            hoh=self.hoh,
            )

