from flask import render_template


def get_documentation():
    return render_template("rapidoc.html")