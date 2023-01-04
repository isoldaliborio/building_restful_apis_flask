from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(message = 'Hello World!')


@app.route('/super_simple')
def super_simple():
    return jsonify(message = "hello from the app api training")


@app.route("/not_found")
def not_found():
    return jsonify(message = "That resource was not found"), 404


if __name__ == '__main__':
    app.run()
