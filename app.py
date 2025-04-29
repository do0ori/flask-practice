from flask import Flask, jsonify, request

app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
