from flask import Flask, render_template
from pipeline.model import model
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "Welcome!"


@app.route('/print1')
def print1():
    return str(model.rand_num())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
