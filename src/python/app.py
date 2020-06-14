import os
from flask import Flask, render_template, request, redirect

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


@app.route("/routing/<name>/<int:num>")
def dynamic_routing(name, num: int):
    return render_template('dynamic-routing.html', name=name, num=num)


@app.route("/http-requests", methods=["GET", "POST"])
def requests():
    if request.method == "POST":
        name = request.form["name"]
        number = request.form["number"]
        url = "/routing/" + name + "/" + number
        return redirect(url)
    else:
        get_val = request.args.get("get_val")
        return render_template('request.html', get_val=get_val)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=80)