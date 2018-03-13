import unittest

class TestSongCompose(unittest.TestCase):
    def test_compose_import(self):
        """
        パッケージがimportできること
        """
        import compose_set
        self.assertTrue(compose_set)

    def test_create_song(self):
        """
        曲を作れること
        """
        import compose_set
        song = compose_set.create_song()
        self.assertTrue(song)

    def test_create_song_instance(self):
        """
        作った曲がSongインスタンスであること
        """
        import compose_set
        song = compose_set.create_song()
        self.assertIsInstance(song, compose_set.Song)

    def test_create_song_with_name(self):
        """
        作った曲に名前をつけられること
        """
        import compose_set
        song_name = "作った曲の名前"
        song = compose_set.create_song(song_name)
        self.assertEqual(song.name, song_name)

    def test_add_section(self):
        """
        曲の中にセクションを追加できること
        """
        import compose_set
        song = compose_set.create_song()
        self.assertFalse(song.section)
        song.add_section()
        self.assertTrue(song.section)

    def test_add_section_instance(self):
        """
        曲の中に追加したセクションのインスタンスが、Sectionであること
        """
        import compose_set
        song = compose_set.create_song()
        song.add_section()
        self.assertIsInstance(song.section[0], compose_set.Section)

    def test_create_section(self):
        """
        Sectionを単体で作成できること
        """
        import compose_set
        section = compose_set.Section()
        self.assertIsInstance(section, compose_set.Section)
