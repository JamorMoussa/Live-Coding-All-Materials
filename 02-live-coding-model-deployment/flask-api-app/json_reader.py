import json
from pathlib import Path
from channel import Channel


class JsonReader:

    def __init__(self):

        self.channels: list[Channel] = []

    def all(self):
        return [ch.to_dict() for ch in self.channels]
    
    def add_channel(self, **kwargs):
        self.channels.append(Channel(**kwargs))

    def read_json(self, path: str):

        with open(path, "rb") as f:

            channels = json.load(f)

            for channel_dict in channels:

                ch = Channel()

                ch.from_dict(channel_dict)

                self.channels.append(ch)


