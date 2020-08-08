from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def say_hello():
    return "HelloThere!"


print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    print("Goodbye, World!")
