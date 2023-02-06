from app import db

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    tenant_id = db.Column(db.String)
    title = db.Column(db.String)
    decription = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    cost = db.Column(db.Integer)
    transportation = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "user_id" :self.user_id,
            "tenant_id":self.tenant_id,
            "title": self.title,
            "decription":self.decription,
            "date": self.date,
            "time": self.time,
            "cost": self.cost,
            "transportation": self.transportation
        }