def create_song(name="Unknown Song"):
    return Song(name)

class Song():
    def __init__(self, name):
        self.name = name
        self.section = []

    def add_section(self):
        self.section.append(Section())

class Section():
    pass
