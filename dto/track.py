
class Track:
    def __init__(self, id, name, artist, album, duration_ms, popularity, explicit, url):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.duration_ms = duration_ms
        self.popularity = popularity
        self.explicit = explicit
        self.url = url

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist,
            'album': self.album,
            'duration_ms': self.duration_ms,
            'popularity': self.popularity,
            'explicit': self.explicit,
            'url': self.url
        }