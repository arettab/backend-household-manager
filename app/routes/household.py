from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

bp = Blueprint("households", __name__)




