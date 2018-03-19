import unittest


class TestMileStone2(unittest.TestCase):
    def test_scale_1t_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(1)
        self.assertEqual(note.name, 'C')

    def test_scale_1t_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(1)
        self.assertEqual(note.name, 'D')

    def test_scale_1t_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(1)
        self.assertEqual(note.name, 'E')

    def test_scale_1t_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(1)
        self.assertEqual(note.name, 'F')

    def test_scale_1t_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(1)
        self.assertEqual(note.name, 'G')

    def test_scale_1t_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(1)
        self.assertEqual(note.name, 'A')

    def test_scale_1t_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで１の音がわかる
        キー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(1)
        self.assertEqual(note.name, 'B')

    def test_scale_2nd_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(2)
        self.assertEqual(note.name, 'D')

    def test_scale_2nd_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(2)
        self.assertEqual(note.name, 'E')

    def test_scale_2nd_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(2)
        self.assertEqual(note.name, 'F_')

    def test_scale_2nd_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(2)
        self.assertEqual(note.name, 'G')

    def test_scale_2nd_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(2)
        self.assertEqual(note.name, 'A')

    def test_scale_2nd_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(2)
        self.assertEqual(note.name, 'B')

    def test_scale_2nd_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで2の音がわかる
        キー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(2)
        self.assertEqual(note.name, 'C_')

    def test_scale_3rd_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(3)
        self.assertEqual(note.name, 'E')

    def test_scale_3rd_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(3)
        self.assertEqual(note.name, 'F_')

    def test_scale_3rd_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(3)
        self.assertEqual(note.name, 'G_')

    def test_scale_3rd_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(3)
        self.assertEqual(note.name, 'A')

    def test_scale_3rd_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(3)
        self.assertEqual(note.name, 'B')

    def test_scale_3rd_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(3)
        self.assertEqual(note.name, 'C_')

    def test_scale_3rd_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで3の音がわかる
        キー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(3)
        self.assertEqual(note.name, 'D_')

    def test_scale_4th_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(4)
        self.assertEqual(note.name, 'F')

    def test_scale_4th_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(4)
        self.assertEqual(note.name, 'G')

    def test_scale_4th_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(4)
        self.assertEqual(note.name, 'A')

    def test_scale_4th_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(4)
        self.assertEqual(note.name, 'A_')

    def test_scale_4th_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(4)
        self.assertEqual(note.name, 'C')

    def test_scale_4th_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(4)
        self.assertEqual(note.name, 'D')

    def test_scale_4th_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで4の音がわかる
        キー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(4)
        self.assertEqual(note.name, 'E')

    def test_scale_5th_key_in_C_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー C の場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        note = scale.note(5)
        self.assertEqual(note.name, 'G')

    def test_scale_5th_key_in_D_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー D の場合
        """
        import compose.core
        scale = compose.core.Scale(key="D")
        note = scale.note(5)
        self.assertEqual(note.name, 'A')

    def test_scale_5th_key_in_E_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー E の場合
        """
        import compose.core
        scale = compose.core.Scale(key="E")
        note = scale.note(5)
        self.assertEqual(note.name, 'B')

    def test_scale_5th_key_in_F_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー F の場合
        """
        import compose.core
        scale = compose.core.Scale(key="F")
        note = scale.note(5)
        self.assertEqual(note.name, 'C')

    def test_scale_5th_key_in_G_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー G の場合
        """
        import compose.core
        scale = compose.core.Scale(key="G")
        note = scale.note(5)
        self.assertEqual(note.name, 'D')

    def test_scale_5th_key_in_A_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー A の場合
        """
        import compose.core
        scale = compose.core.Scale(key="A")
        note = scale.note(5)
        self.assertEqual(note.name, 'E')

    def test_scale_5th_key_in_B_major_scale(self):
        """
        あるキーのメジャースケールで5の音がわかる
        キー B の場合
        """
        import compose.core
        scale = compose.core.Scale(key="B")
        note = scale.note(5)
        self.assertEqual(note.name, 'F_')

    def test_get_note_list_in_C_majar_scale(self):
        """
        あるキーのメジャースケールの音階がわかる
        C メジャースケールの場合
        """
        import compose.core
        scale = compose.core.Scale(key="C")
        notes = scale.notes
        self.assertIn('C', notes)
        self.assertIn('D', notes)
        self.assertIn('E', notes)
        self.assertIn('F', notes)
        self.assertIn('G', notes)
        self.assertIn('A', notes)
        self.assertIn('B', notes)

    def test_get_note_list_in_C__majar_scale(self):
        """
        あるキーのメジャースケールの音階がわかる
        C# メジャースケールの場合
        """
        import compose.core
        scale = compose.core.Scale(key="C_")
        notes = scale.notes
        self.assertIn('C_', notes)
        self.assertIn('D_', notes)
        self.assertIn('F', notes)
        self.assertIn('F_', notes)
        self.assertIn('G_', notes)
        self.assertIn('A_', notes)
        self.assertIn('C', notes)

    def test_get_note_list_in_G__majar_scale(self):
        """
        あるキーのメジャースケールの音階がわかる
        G# メジャースケールの場合
        """
        import compose.core
        scale = compose.core.Scale(key="G_")
        notes = scale.notes
        self.assertIn('G_', notes)
        self.assertIn('A_', notes)
        self.assertIn('C', notes)
        self.assertIn('C_', notes)
        self.assertIn('D_', notes)
        self.assertIn('F', notes)
        self.assertIn('G', notes)
