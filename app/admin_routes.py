from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.admin import Admin
import bcrypt

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# register admin
@admin_bp.route("/register", methods=["POST"])
def register():
    admin_name = request.json.get('admin_name', None)
    password = request.json.get('password', None)

    if not admin_name:
        return 'Missig admin name!', 400
    if not password:
        return 'Missig password!', 400    
        
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    admin = Admin(admin_name=admin_name, password=hashed.decode("utf8"))

    db.session.add(admin)
    db.session.commit()
    return f'welcome {admin_name}'


# check login
@admin_bp.route("/login", methods=["POST"])
def login():
    admin_name = request.json.get('admin_name', None)
    password = request.json.get('password', None)

    if not admin_name:
        return 'Missig admin name!', 400
    if not password:
        return 'Missig password!', 400

    admin = Admin.query.filter_by(admin_name=admin_name).first()
    if not admin:
        return 'Admin not found!', 404
    my_hash = bcrypt.checkpw(password.encode('utf8'), admin.password.encode('utf8'))
    if my_hash:
        return f'Welcome back {admin_name}'
    else:
        return 'Incorrect Password!'


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