from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_decorator():
        return f"<b>{function()}</b>"
    return wrapper_decorator

def make_italic(function):
    def wrapper_decorator():
        return f"<em>{function()}</em>"
    return wrapper_decorator

def make_underline(function):
    def wrapper_decorator(*args):
        return f"<u>{function(args[0])}</u>"
    return wrapper_decorator
# @app.route("/")
# @make_italic
# @make_bold
# @make_underline
# def hello_world():
#     return "<p>Hello, World!</p>"

#writing  a variable in a url

@app.route("/<name>")
@make_underline
def greeting(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug= True)
