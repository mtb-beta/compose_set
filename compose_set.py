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
        self.chord = ChordManager(key=self.key)
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
    def __init__(self, key="C"):
        self.step = 0
        self.chord_progression = []
        self.key = key

    def progress(self, chord=None, root=1):
        if chord:
            self.chord_progression.append(chord)
        else:
            self.chord_progression.append(self.diatonic_code(root))

    def next(self):
        next_chord = self.chord_progression[self.step]
        self.step += 1
        return next_chord

    def diatonic_code(self, root):
        if root == 1:
            return 'C'
        elif root == 2:
            return 'Dm7'
        elif root == 3:
            return 'Em7'
        elif root == 4:
            return 'F'
        elif root == 5:
            return 'G7'
        elif root == 6:
            return 'Am7'
        elif root == 7:
            return 'Bm7(-5)'

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
