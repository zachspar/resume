import os

from flask_sslify import SSLify
from flask import Flask, render_template

app = Flask(__name__)

if "DYNO" in os.environ:
    sslify = SSLify(app)


@app.route('/')
def index():
    return render_template('home/index.html')


if __name__ == '__main__':
    app.run()
