import unittest
from music_library import Song, PlayList


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Osydeni dushi", "Lili_Ivanova", "Ne_znam", "3:33")
        self.song2 = Song("Jiva rana", "Slavi_Trifonov", "Novite_varvari", "4:13")

    def test_get_length_seconds(self):
        self.assertEqual(self.song1.get_length(seconds=True), 213)

    def test_get_length_minutes(self):
        self.assertEqual(self.song2.get_length(minutes=True), 4)

    def test_get_length_hours(self):
        self.assertEqual(self.song1.get_length(hours=True), 0)

    def test_get_length(self):
        self.assertEqual(self.song2.get_length(), "4:13")

    def test_str(self):
        self.assertEqual(str(self.song1), "Lili_Ivanova - Osydeni dushi from Ne_znam - 3:33")


class TestPlayList(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Osydeni dushi", "Lili_Ivanova", "Ne_znam", "3:33")
        self.song2 = Song("Jiva rana", "Slavi_Trifonov", "Novite_varvari", "4:13")
        self.playlist = PlayList("pl1")

    def test_total_length(self):
        self.playlist.add_song(self.song1)
        self.assertEqual(self.playlist.total_length(), "0:03:33")

    def test_artists(self):
        song3 = Song("Neka me boli", "Slavi_Trifonov", "Ideq_nqmam", "5:02")
        song4 = Song("Rekviem", "Slavi_Trifonov", "Ideq_nqmam2", "3:51")
        self.playlist.add_songs([self.song1, self.song2, song3, song4])
        self.assertEqual(self.playlist.artists(), {"Slavi_Trifonov": 3, "Lili_Ivanova": 1})

if __name__ == '__main__':
    unittest.main()
