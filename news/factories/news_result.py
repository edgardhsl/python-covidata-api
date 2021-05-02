
import json

class NewsResult:

    title: str
    description: str
    thumbnailUrl: str
    publisher: str
    url: str

    def __init__(self, title, description, thumbnail, publisher, url):
        self.title      = title
        self.description = description
        self.thumbnail  = thumbnail
        self.publisher  = publisher
        self.url        = url

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

