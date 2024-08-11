

class Channel:

    def __init__(
        self, 
        id: str = "id",
        name: str = "name",
        tags: list[str] = [],
        description: str = "some description"
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
            "description": self.description,
        }
    
    def from_dict(self, channel_dict: dict):
        self.id = channel_dict["id"]
        self.name = channel_dict["name"]
        self.tags = channel_dict["tags"]
        self.description = channel_dict["description"]

    
    def __repr__(self) -> str:
        return f"Channel({str(self.to_dict())})"