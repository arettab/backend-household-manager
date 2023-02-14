from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    userId = db.relationship("User", backref="user", lazy=True)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
        name=data_dict["name"])

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )
# Title, Description, EventId, TimeDate, Transportation, Cost,userId