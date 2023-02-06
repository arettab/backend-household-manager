from app import db
from flask import Blueprint, request, jsonify, make_response, abort

bp = Blueprint("events", __name__, url_prefix="/events")