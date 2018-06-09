import enum

@enum.unique
class ChromaticScale(enum.Enum):
    """
    クロマチックスケール
    # は _ で表示している。
    """
    C = 0
    C_ = 1
    D = 2
    D_ = 3
    E = 4
    F = 5
    F_ = 6
    G = 7
    G_ = 8
    A = 9
    A_ = 10
    B = 11

# メジャースケール
MajarScale = {
    1 : 0,
    2 : 2,
    3 : 4,
    4 : 5,
    5 : 7,
    6 : 9,
    7 : 11,
}


class Scale:
    def __init__(self, key="C", scale_type=MajarScale):
        self.key = key
        self.scale_type = scale_type

    def note(self, number):
        # キーがずれている数だけオフセットを設定する
        self.offset = ChromaticScale[self.key].value
        # numberで指定された度数だけずらす。
        note = (self.scale_type[number] + self.offset) % 12
        return ChromaticScale(note)

    @property
    def notes(self):
        return [ note.name for note in ChromaticScale] 

    def diatonic(self, number):
        # 1~に納めるために一時的にnumberを-1して後で足している。
        number = number - 1
        diatonic_num = len(self.scale_type)
        return [
            self.note((number) % diatonic_num + 1).name,
            self.note((number + 2 ) % diatonic_num + 1).name,
            self.note((number + 4 ) % diatonic_num + 1).name
        ]

    def diatonic_number(self, note):
        """
        ノート名を渡すと、ダイアトニック番号を返す
        key C で Cを渡すと1が返ってくるような感じ
        """
        for key in self.scale_type:
            if self.scale_type[key] == ChromaticScale[note].value:
                return key

class Chord:
    def __init__(self, tones, root):
        self.tones = tones
        self.root = root

    @property
    def name(self):
        if self.has_minor_3rd():
            return "{}m".format(self.root)
        else:
            return self.root

    def has_minor_3rd(self):
        """
        短３度が含まれているか
        """
        for tone in self.tones:
            distance = (ChromaticScale[tone].value - ChromaticScale[self.root].value)%12
            if distance == 3:
                return True

