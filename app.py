import os
import tomllib

from flask_sslify import SSLify
from flask import Flask, render_template

app = Flask(__name__)

with open("config.toml") as f:
    template_config = tomllib.load(f)

if "DYNO" in os.environ:
    sslify = SSLify(app)


@app.route("/")
def index():
    return render_template("home/index.html", **template_config)


if __name__ == "__main__":
    app.run()
