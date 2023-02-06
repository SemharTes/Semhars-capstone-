from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.admin import Admin

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# validate_model
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"invalid model id {model_id}"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"model id {model_id} not found"}, 404))
    
    return model
# create admin  
@admin_bp.route("", methods=["POST"])
def create_admin():
    request_body = request.get_json()

    new_admin = Admin.instance_from_json(request_body)

    db.session.add(new_admin)
    db.session.commit()

    return {"admin":new_admin.to_dict()}, 201

# get all admins
@admin_bp.route("", methods=["GET"])
def get_all_admins():
    admins = Admin.query.all()
    response = [admin.to_dict() for admin in admins]

    return jsonify(response)


# delete an admin
@admin_bp.route("/<admin_id>", methods=["DELETE"])
def delete_admin(admin_id):
    admin = validate_model(Admin, admin_id)
    
    db.session.delete(admin)
    db.session.commit()
    
    return make_response("success deleting.",200)