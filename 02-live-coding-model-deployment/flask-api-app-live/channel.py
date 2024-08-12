import json 


class Channel:

    def __init__(
        self,
        id: str = None,
        name: str = None,
        tags: list[str] = None, 
        description: str = None, 
    ): 
        
        self.id = id
        self.name = name 
        self.tags = tags 
        self.description = description

    def to_dict(self):

        return {
            "id": self.id, 
            "name": self.name,
            "tags": self.tags,
            "description": self.description
        }
    
    def from_dict(self, channel_dict):

        self.id = channel_dict["id"]
        self.name = channel_dict["name"]
        self.tags = channel_dict["tags"]
        self.description = channel_dict["description"]

    
    def __repr__(self) -> str:
        return f"Channel( id = {self.id}, name= {self.name})"



class ChannelList:

    def __init__(self):

        self.channels: list[Channel] = []


    def get_all(self) -> list[Channel]:
        return self.channels
    

    def get_channel_by_id(self, id: str):

        for ch in self.channels:

            if ch.id == id: return ch

        return None

    def load_json(self, path: str):


        with open(path, "rb") as f:

            channels_list = json.load(f)


        for ch_dict in channels_list:

            ch = Channel()

            ch.from_dict(ch_dict)

            self.channels.append(ch)


