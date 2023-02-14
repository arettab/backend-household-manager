from app import db

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_hoh = db.Column(db.Boolean, default=False)
    

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
        userId = data_dict["userId"],
        name = data_dict["name"],
        is_hoh = data_dict["is_hoh"],
        )

    def to_dict(self):
        user_to_dict = {}
        user_to_dict["name"] = self.name,
        user_to_dict["is_hoh"] = self.is_hoh,

        return user_to_dict
