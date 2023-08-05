from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/law")
def law():
    return render_template("law.html")


if __name__ == "__main__":
    app.run(debug=True)
