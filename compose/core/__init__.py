import enum


class ChromaticScale(enum.Enum):
    """
    クロマチックスケール
    # は _ で表示している。
    """
    C = 1
    C_ = 2
    D = 3
    D_ = 4
    E = 5
    F = 6
    F_ = 7
    G = 8
    G_ = 9
    A = 10
    A_ = 11
    B = 12

class Scale:
    def __init__(self, key="C"):
        self.key = key

    def note(self, number):
        self.offset = ChromaticScale[self.key].value - 1
        return ChromaticScale(number + self.offset)

