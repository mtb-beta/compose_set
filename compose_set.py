def create_song(name):
    return Song(name)

class Song():
    def __init__(self, name):
        self.name = name
