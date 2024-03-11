

class Track:
    def __init__(self, id, name, artist, album, duration, popularity, explicit, url):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration
        self.popularity = popularity
        self.explicit = explicit
        self.url = url

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist,
            'album': self.album,
            'duration': self.duration,
            'popularity': self.popularity,
            'explicit': self.explicit,
            'url': self.url
        }