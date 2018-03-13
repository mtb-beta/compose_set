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

    def test_create_song(self):
        """
        作った曲がSongインスタンスであること
        """
        import compose_set
        song = compose_set.create_song()
        self.assertIsInstance(song, compose_set.Song)

    def test_create_song(self):
        """
        作った曲に名前をつけられること
        """
        import compose_set
        song_name = "作った曲の名前"
        song = compose_set.create_song(song_name)
        self.assertEqual(song.name, song_name)
