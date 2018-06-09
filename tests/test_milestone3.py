import unittest


class TestMileStone3(unittest.TestCase):
    def test_scale_diatonic_number_C_in_C_major_scale(self):
        """
        あるキーのメジャースケールでCのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('C')
        self.assertEqual(diatonic_number, 1)

    def test_scale_diatonic_number_D_in_C_major_scale(self):
        """
        あるキーのメジャースケールでDのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('D')
        self.assertEqual(diatonic_number, 2)

    def test_scale_diatonic_number_E_in_C_major_scale(self):
        """
        あるキーのメジャースケールでEのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('E')
        self.assertEqual(diatonic_number, 3)

    def test_scale_diatonic_number_F_in_C_major_scale(self):
        """
        あるキーのメジャースケールでFのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('F')
        self.assertEqual(diatonic_number, 4)

    def test_scale_diatonic_number_G_in_C_major_scale(self):
        """
        あるキーのメジャースケールでGのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('G')
        self.assertEqual(diatonic_number, 5)

    def test_scale_diatonic_number_A_in_C_major_scale(self):
        """
        あるキーのメジャースケールでAのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('A')
        self.assertEqual(diatonic_number, 6)

    def test_scale_diatonic_number_B_in_C_major_scale(self):
        """
        あるキーのメジャースケールでBのノート番号がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        diatonic_number = scale.diatonic_number('B')
        self.assertEqual(diatonic_number, 7)
