import os

from dotenv import load_dotenv
from flask import json, jsonify

load_dotenv()


def get_json():

    json_file = os.path.abspath(__file__).split("app")[0] + "app/static/rapidoc.json"
    with open(json_file, "r") as file:
        data = json.load(file)
    return jsonify(data)
