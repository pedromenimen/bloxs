import os

from dotenv import load_dotenv
from flask import json, jsonify

load_dotenv()


def get_json():

    json_file = os.path.abspath(__file__).split("app")[0]
    print('\n\n\n\n',json_file,'\n\n\n\n')
    with open(json_file, "r") as file:
        data = json.load(file)
    return jsonify(data)
