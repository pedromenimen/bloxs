import os
from flask import render_template


def get_documentation():
    url = os.getenv("BASE_URL")+"/api/rapidoc-json/"
    return render_template("rapidoc.html", url=url)