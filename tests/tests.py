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
