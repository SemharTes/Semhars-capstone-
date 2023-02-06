from app import db
from flask import make_response, abort

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String)
    password = db.Column(db.String)


    @classmethod
    def instance_from_json(cls, request_body):
        try:
            new_admin = Admin(
                admin_name=request_body["admin_name"],
                password=request_body["password"],
                )
            return new_admin
        except:
            abort(make_response({"details": "Invalid data"}, 400))
    
    def to_dict(self):
        return {
            
            "admin_id": self.admin_id,
            "admin_name": self.admin_name,
            "password": self.password
        }
    
    