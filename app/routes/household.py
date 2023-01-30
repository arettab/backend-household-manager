from app import db
from flask import Blueprint, request, jsonify, make_response, abort
from app.models.event import Event
from app.models.household import Household

bp = Blueprint("households", __name__, url_prefix="/households")

@bp.route("", methods=["POST"])
def create_household():
    request_body = request.get_json()
    new_household = Household.from_dict(request_body)

    db.session.add(new_household)
    db.session.commit()

    return make_response(f"Household {new_household.name} successfully created")


