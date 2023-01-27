from app import db

class Event(db.Model):
    event_id = db.Column(db.Interger, primanry_key=True, autoincrement=True)
    user_id = db.Column(db.Interger)
    tenant_id = db.Column(db.String)
    title = db.Column(db.String)
    decription = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.Sting)
    cost = db.Column(db.Interger)
    transportation = db.Column(db.Bool)

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