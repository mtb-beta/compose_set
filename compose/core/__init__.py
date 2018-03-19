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
        # numberで指定された度数だけずらす。同じノートが1度なので-1する
        note = (self.scale_type[number] + self.offset)%12
        return ChromaticScale(note)

    @property
    def notes(self):
        return [ note.name for note in ChromaticScale] 



