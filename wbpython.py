from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello, world!!!!!"
    headline = "Hello World!!!"
    now = datetime.datetime.now()
    new_year = now.month == 7 and now.day == 8
    names = ['vitto', 'pipppo', 'topolino','paperino']
    return render_template("index.html", names = names)

@app.route("/bye")
def bye():
    headline = "Bye World!!!"
    return render_template("index.html", headline=headline)


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