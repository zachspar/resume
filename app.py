#!/usr/bin/env python3
"""
A tiny Flask app to render a resume template.
"""
from os import environ as _environ
from tomllib import load as _load

from flask import Flask, render_template

app = Flask(__name__)

with open("resume_config.toml", "rb") as f:
    template_config = _load(f)

if "DYNO" in _environ:
    from flask_sslify import SSLify

    SSLify(app)


@app.route("/")
def index():
    return render_template("home/index_template.html", **template_config)


if __name__ == "__main__":
    app.run()
