from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

bp = Blueprint("households", __name__)

userfront_test_key = os.environ.get("USERFRONT_TEST_KEY")


@bp.route("/households", methods=["POST"])
def add_household():
    url = "https://api.userfront.com/v0/tenants"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer " +userfront_test_key
    }

    request_body = requests.get_json()

    data = {
        "name": request_body.get("name"),
        "data": {
            "events":[]}
        }

    response = requests.post(
        url, data=data, headers=headers)
    
    

    return response.text

@bp.route("/households/<household_id>/<user_id>", methods=["PUT"])
def add_user_to_household(tenantId, userId):

    url = f"https://api.userfront.com/v0/tenants/{tenantId}"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + userfront_test_key
    }

    response = requests.get(url, headers=headers)
    current_data = response.json()

    current_data['data']['events'].append({userId: []})

    response = requests.put(url, data=current_data, headers=headers)

    return response.text




