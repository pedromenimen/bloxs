from app.static import rapidoc_file
from flask import json, jsonify



def get_json():

    with open(rapidoc_file, "r") as file:
        data = json.load(file)
    return jsonify(data)
