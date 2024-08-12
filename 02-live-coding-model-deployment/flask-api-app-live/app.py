from flask import Flask, jsonify

from channel import Channel, ChannelList

app = Flask(__file__)


channel_list = ChannelList()

channel_list.load_json("channels.json")


@app.route("/all", methods=["GET"])
def get_all():

    return jsonify([ch.to_dict() for ch in channel_list.get_all()])


@app.route("/channel/<channel_id>")
def get_channel_by_id(channel_id):
    
    try: 
        ch = channel_list.get_channel_by_id(id= channel_id)

        return jsonify(ch.to_dict())
    
    except: 
        return jsonify({
            "message": "Error, Channel is not found", 
            "other": None
        })



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



