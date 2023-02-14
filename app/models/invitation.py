from app import db

class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    household_id = db.Column(db.Integer, db.ForeignKey('household.id'))

@classmethod
def from_dict(cls, data_dict):
        return cls(
        email = data_dict["email"],
        household_id =data_dict["household"]
        )

def to_dict(self):
        return dict(
            id=self.id,
            email=self.name
        )
