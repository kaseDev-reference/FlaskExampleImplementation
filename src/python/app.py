import os
from flask import Flask, render_template

template_dir = os.path.abspath('../../templates')
static_dir = os.path.abspath('../../static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/templating")
def templating():
    name = 'John Doe'
    items = ["first", "second", "third", "fourth", 'fifth', 'sixth']
    return render_template('templating.html', content=name, items=items)


@app.route("/routing")
def routing():
    return render_template('routing.html')


@app.route("/html-requests")
def requests():
    return render_template('request.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=80)