class Song():
    def __init__(
            self,
            name="Unknown Song",
            thema="UnKnown"
        ):
        self.name = name
        self.thema = thema
        self.section = []

    def add_section(self):
        self.section.append(Section())

class Section():
    def __init__(self, name="Unknown Section"):
        self.name = name
