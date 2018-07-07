from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello, world!!!!!"
    return render_template("page0.html")
# @app.route("/david")
# def david():
#     return "Hello David"
#
# @app.route("/maria")
# def maria():
#     return "Hello Maria"
#
# @app.route("/<string:name>")
# def hello(name):
#     name = name.capitalize()
#     return "<h1>Hello, {}<h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)