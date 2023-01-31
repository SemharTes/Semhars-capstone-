from app import db
from app.models.symptom import Symptom
from flask import Blueprint, request, jsonify, make_response, abort

symptoms_bp = Blueprint("symptoms", __name__, url_prefix="/symptoms")

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

# get all symptoms
@symptoms_bp.route("", methods=["GET"])
def get_all_symptoms():
    # response = [symptom.to_dict() for symptom in symptoms]
    title_param = request.args.get("title")
    if title_param:
        symptoms = Symptom.query.filter_by(title=title_param)
    else:
        symptoms = Symptom.query.all()
    
    response = [symptom.to_dict() for symptom in symptoms]
    return jsonify(response)


# get one symptom
@symptoms_bp.route("/<symptom_id>", methods=["GET"])
def get_a_symptom(symptom_id):
    symptom = Symptom.query.get(symptom_id)
    return symptom.to_dict()


# post symptoms
@symptoms_bp.route("", methods=["POST"])
def create_symptom():
    request_body = request.get_json()

    new_symptom = Symptom.instance_from_json(request_body)

    db.session.add(new_symptom)
    db.session.commit()

    return {"symptom":new_symptom.to_dict()}, 201

# delete a symptom 
@symptoms_bp.route("/<symptom_id>", methods=["DELETE"])
def delete_symptom(symptom_id):
    symptom = validate_model(Symptom, symptom_id)
    
    db.session.delete(symptom)
    db.session.commit()
    
    return make_response("success deleting",200)