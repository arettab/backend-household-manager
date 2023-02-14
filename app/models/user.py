from app import db

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    is_hoh = db.Column(db.Boolean, default=False)
    household_id = db.Column(db.Integer, db.ForeignKey('household.id'))
    

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
        userId = data_dict["userId"],
        username = data_dict["username"],
        is_hoh = data_dict["is_hoh"],
        household_id =data_dict["household"]
        )

    def to_dict(self):
        user_to_dict = {}
        user_to_dict["username"] = self.username,
        user_to_dict["is_hoh"] = self.is_hoh,
        user_to_dict["household_id"] = self.household_id

        return user_to_dict
