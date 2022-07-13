from app.static import rapidoc_file
from dotenv import load_dotenv
from flask import json, jsonify

load_dotenv()


def get_json():

    print("\n\n\n\n", rapidoc_file, "\n\n\n\n")
    with open(rapidoc_file, "r") as file:
        data = json.load(file)
    return jsonify(data)
