from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

bp = Blueprint("users", __name__)

userfront_test_key = os.environ.get("USERFRONT_TEST_KEY")


@bp.route("/users/<userId>", methods=["GET"])
def get_user(userId):
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

@bp.route("/users/invite", methods=["POST"])
def invite_users(tenantId, email, name):

    url = f"https://api.userfront.com/v0/tenants/{tenantId}/roles/invite"
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer uf_test_admin_vbqvm99n_6515a9308420587664b486a4a47b6b59"
        }

    data = {
        "email": email,
        "name": name,
        "roles": [
            "member"
            ],
        "options": {}
        }

    response = requests.post(url, data=data, headers=headers)

    return response.text
