from app import db

class Household(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
        name=data_dict["name"])

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )
