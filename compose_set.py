class Song:
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

class Section:
    def __init__(self, name="Unknown Section"):
        self.name = name
        self.elevation = 5
        self.measure = 8
        self.beat = Beat()
        self.chord = ChordManager()

class ChordManager:
    def __init__(self):
        self.step = 0
        self.chord_progression = []

    def progress(self, chord):
        self.chord_progression.append(chord)

    def next(self):
        next_chord = self.chord_progression[self.step]
        self.step += 1
        return next_chord

    @property
    def progression(self):
        return self.chord_progression

class Beat:
    def __init__(self, name="Unknow Beat"):
        self.name = name

