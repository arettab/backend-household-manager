from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

bp = Blueprint("roles", __name__)

userfront_test_key = os.environ.get("USERFRONT_TEST_KEY")

@bp.route("/users/<tenantId>/<userId>", methods=["PUT"])
def add_hoh(tenantId,userId):
    url = f"https://api.userfront.com/v0/tenants/{tenantId}/users/{userId}/roles"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer" + userfront_test_key}

    data = {
        "roles": [
            "admin",
            "member"
        ]
        }


    response = requests.put(url, data=data, headers=headers)
    return response.text

@bp.route("/users/<tenantId>/<userId>", methods=["POST"])
def add_member():

    url = "https://api.userfront.com/v0/tenants/{tenantId}/roles/invite"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer" + userfront_test_key
        }
    data = {
        "email": ,
        "name": ,
        "roles": [
            "member"
        ],
        "options": {}
        }
    response = requests.post(url, data=data, headers=headers)

    return response.text