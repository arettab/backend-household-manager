from app import db
from app.models.user import User
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/id", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.to_dict()), 200

@bp.route("", methods=["POST"])
def add_user(id):
    request_body = request.get_json()
    new_user = User.from_dict(request_body)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201