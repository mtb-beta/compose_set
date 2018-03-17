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
        song = compose_set.Song()
        self.assertTrue(song)

    def test_create_song_instance(self):
        """
        作った曲がSongインスタンスであること
        """
        import compose_set
        song = compose_set.Song()
        self.assertIsInstance(song, compose_set.Song)

    def test_create_song_with_name(self):
        """
        作った曲に名前をつけられること
        """
        import compose_set
        song_name = "作った曲の名前"
        song = compose_set.Song(song_name)
        self.assertEqual(song.name, song_name)

    def test_create_song_with_name(self):
        """
        作った曲にテーマを設定できること
        """
        import compose_set
        song_name = "作った曲の名前"
        song_thema = "この曲のテーマ"
        song = compose_set.Song(name=song_name,thema=song_thema)
        self.assertEqual(song.thema, song_thema)

    def test_add_section(self):
        """
        曲の中にセクションを追加できること
        """
        import compose_set
        song = compose_set.Song()
        self.assertFalse(song.section)
        song.add_section()
        self.assertTrue(song.section)

    def test_add_section_instance(self):
        """
        曲の中に追加したセクションのインスタンスが、Sectionであること
        """
        import compose_set
        song = compose_set.Song()
        song.add_section()
        self.assertIsInstance(song.section[0], compose_set.Section)

    def test_create_section(self):
        """
        Sectionを単体で作成できること
        """
        import compose_set
        section = compose_set.Section()
        self.assertIsInstance(section, compose_set.Section)

    def test_section_setting_measure(self):
        """
        Sectionに小節数を設定できること
        """
        import compose_set
        section = compose_set.Section()
        self.assertEqual(section.measure, 8)
        section.measure = 4
        self.assertEqual(section.measure, 4)

    def test_section_setting_elevation(self):
        """
        Sectionに盛り上がり度合いを設定できること
        """
        import compose_set
        section = compose_set.Section()
        self.assertEqual(section.elevation, 5)
        section.elevation = 10
        self.assertEqual(section.elevation, 10)

    def test_section_setting_beat(self):
        """
        Sectionにビートを設定できること
        """
        import compose_set
        section = compose_set.Section()
        self.assertIsInstance(section.beat, compose_set.Beat)
        beat_name = "ビートの名前"
        section.beat = compose_set.Beat(name=beat_name)
        self.assertEqual(section.beat.name, beat_name)

    def test_section_setting_chrod(self):
        """
        Sectionにコード進行を入力できること
        """
        import compose_set
        section = compose_set.Section()
        section.chord.progress("FM7")
        self.assertEqual(section.chord.next(), "FM7")
        section.chord.progress("G7")
        self.assertEqual(section.chord.next(), "G7")
        section.chord.progress("Em7")
        self.assertEqual(section.chord.next(), "Em7")
        section.chord.progress("Am")
        self.assertEqual(section.chord.next(), "Am")
        self.assertEqual(section.chord.progression, ["FM7","G7","Em7","Am"])

    def test_section_setting_instrument(self):
        """
        Sectionに楽器を追加できること
        """
        import compose_set
        section = compose_set.Section()
        # Guitar 1と言う名前の楽器を追加できること
        section.instrument.add(name="Guitar 1", itype="Guitar")
        self.assertTrue(section.instrument.has("Guitar 1"))
        self.assertTrue(type(section.instrument.get("Guitar 1")), compose_set.Instrument)
        self.assertIsInstance(section.instrument.get("Guitar 1"), compose_set.Guitar)

        # MyBaseと言う名前の楽器を追加できること
        section.instrument.add(name="My Base", itype="Base")
        self.assertTrue(section.instrument.has("My Base"))
        self.assertTrue(type(section.instrument.get("My Base")), compose_set.Instrument)
        self.assertIsInstance(section.instrument.get("My Base"), compose_set.Base)

        # FavoriteDrumと言う名前の楽器を追加できること
        section.instrument.add(name="Favorite Drum", itype="Drum")
        self.assertTrue(section.instrument.has("Favorite Drum"))
        self.assertTrue(type(section.instrument.get("Favorite Drum")), compose_set.Instrument)
        self.assertIsInstance(section.instrument.get("Favorite Drum"), compose_set.Drum)

        # ３点測量
        self.assertFalse(section.instrument.has("Voval melody"))
        with self.assertRaises(KeyError):
            self.assertFalse(section.instrument.get("Voval melody"))
        self.assertEqual(section.instrument.count, 3)

