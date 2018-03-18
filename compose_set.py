class Song:
    def __init__(
            self,
            name="Unknown Song",
            thema="UnKnown",
            tempo=120,
            key='C'
        ):
        self.name = name
        self.thema = thema
        self.section = []
        self.tempo = tempo
        self.key = key

    def add_section(self):
        self.section.append(Section(key=self.key))

class Section:
    def __init__(
            self,
            name="Unknown Section",
            key="C"
        ):
        self.name = name
        self.elevation = 5
        self.measure = 8
        self.key = key
        self.beat = Beat()
        self.chord = ChordManager()
        self.instrument = InstrumentManager()

class InstrumentManager:
    def __init__(self):
        self.instruments = {}

    def add(self, name, itype):
        self.instruments[name] = Instrument(itype=itype)

    def has(self, name):
        return name in self.instruments

    def get(self, name):
        return self.instruments[name]

    @property
    def count(self):
        return len(self.instruments)

class Instrument:
    def __init__(self, itype):
        self.itype = itype

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
    def __init__(self, name="Unknow Beat", template=None):
        self.name = name
        self.instrument = InstrumentManager()
        if template == "My Test Template":
            self.instrument.add(name="Guitar 1", itype="Guitar")
            self.instrument.add(name="My Base", itype="Base")
            self.instrument.add(name="Favorite Drum", itype="Drum")
        elif template == "My Test Template2":
            self.instrument.add(name="Drums", itype="Drum")

    @property
    def instruments(self):
        return self.instrument.instruments
