from flask import Flask, render_template
from pipeline.model import model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Go to /welcome and /print1 pages."


@app.route('/welcome', methods=['GET'])
def welcome():
    return "Welcome!"


@app.route('/print1', methods=['GET', 'POST'])
def print1():
    return str(model.rand_num())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
