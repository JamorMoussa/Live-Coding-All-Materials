from flask import Flask, jsonify, request
from json_reader import JsonReader

app = Flask(__file__)


jr = JsonReader()
jr.read_json("./channels.json")


@app.route("/all", methods=["GET"])
def get_all():
    return jsonify(jr.all())


@app.route("/add", methods=["POST"])
def add_channel():

    jr.add_channel(**request.json)

    return jsonify({
        "message": "success"
    })



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)