from flask import Blueprint, request, jsonify, make_response, abort
import os
from dotenv import load_dotenv
import requests
from app import db
from app.models.user import User

load_dotenv()

bp = Blueprint("users", __name__, url_prefix="/users")

userfront_test_key = os.environ.get("USERFRONT_TEST_KEY")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model


@bp.route("/proxy/<userId>", methods=["GET"])
def get_user_from_api(userId):
    url = f"https://api.userfront.com/v0/users/{userId}"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer " +userfront_test_key
}

    data = {}
    
    response = requests.get(
        url=url, data=data, headers=headers)
    
    
    return response.text

@bp.route("", methods=["POST"])
def create_user():

    request_body = request.get_json()
    new_user = User.from_dict(request_body)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@bp.route("/<userId>", methods=["GET"])
def get_user_from_db(userId):
    user = validate_model(User, userId)
    return jsonify(user.to_dict()), 200

