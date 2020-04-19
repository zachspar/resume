from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='/static')


@app.route('/')
def index():
    return render_template('home/index.html')


if __name__ == '__main__':
    app.run(debug=True)
