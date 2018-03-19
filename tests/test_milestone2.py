import unittest


class TestMileStone2(unittest.TestCase):
    def test_scale_1t_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(1)
        self.assertEqual(note.name, 'C')

    def test_scale_1t_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(1)
        self.assertEqual(note.name, 'D')

    def test_scale_1t_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(1)
        self.assertEqual(note.name, 'E')

    def test_scale_1t_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(1)
        self.assertEqual(note.name, 'F')

    def test_scale_1t_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(1)
        self.assertEqual(note.name, 'G')

    def test_scale_1t_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(1)
        self.assertEqual(note.name, 'A')

    def test_scale_1t_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        デフォルトキー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(1)
        self.assertEqual(note.name, 'B')

    def test_scale_2nd_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(2)
        self.assertEqual(note.name, 'D')

    def test_scale_2nd_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(2)
        self.assertEqual(note.name, 'E')

    def test_scale_2nd_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(2)
        self.assertEqual(note.name, 'F_')

    def test_scale_2nd_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(2)
        self.assertEqual(note.name, 'G')

    def test_scale_2nd_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(2)
        self.assertEqual(note.name, 'A')

    def test_scale_2nd_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(2)
        self.assertEqual(note.name, 'B')

    def test_scale_2nd_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        デフォルトキー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(2)
        self.assertEqual(note.name, 'C_')
