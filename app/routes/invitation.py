from flask import Blueprint, jsonify, abort, make_response, request
import os
import requests
from app.models.invitation import Invitation
from app import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model


bp = Blueprint("invites", __name__, url_prefix="/invites")

@bp.route("", methods=["POST"])
def create_invite():

    request_body = request.get_json()
    new_invite = Invitation.from_dict(request_body)


    db.session.add(new_invite)
    db.session.commit()

    return "invitation created", 201

@bp.route("", methods=["GET"])
def handle_invite(email):
    invite = Invitation.query.get(email)
    return jsonify(invite.to_dict()), 200


@bp.route("", methods=["DELETE"])
def delete_invite(email):
    invite = Invitation.query.get(email)
    response_body = Invitation.to_dict()

    db.session.delete(invite)
    db.session.commit()

    return "invitation deleted"



