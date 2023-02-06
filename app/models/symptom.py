from app import db
from flask import make_response, abort


class Symptom(db.Model):
    symptom_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    description_url = db.Column(db.String)
    
    @classmethod
    def instance_from_json(cls, request_body):
        try:
            new_symptom = Symptom(
                title=request_body["title"],
                description=request_body["description"],
                description_url=request_body["description_url"]
                )
            return new_symptom
        except:
            abort(make_response({"details": "Invalid data"}, 400))
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "description_url": self.description_url,
            "symptom_id": self.symptom_id,
            "description_url": self.description_url
        }

        # pushing this to github