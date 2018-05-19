from environment import INFO

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def get_env():
    json_data = request.json or {}
    username = json_data.get("username")
    if username:
        INFO["username"] = username
        return jsonify(INFO)
    else:
        return "You must attach your username!"


if __name__ == '__main__':
    app.run()