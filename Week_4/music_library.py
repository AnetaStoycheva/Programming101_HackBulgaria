from random import choice
from tabulate import tabulate
import json
import os
import mutagen
import datetime


def in_seconds(length):

    a = length.split(":")

    if len(a) == 3:
        a[0] = int(a[0]) * 3600
        a[1] = int(a[1]) * 60
        a[2] = int(a[2])

        return a[0] + a[1] + a[2]

    elif len(a) == 2:
        a[0] = int(a[0]) * 60
        a[1] = int(a[1])

        return a[0] + a[1]

    elif len(a) == 1:
        return int(a[0])


def seconds_to_string(all_seconds):
    minutes = all_seconds // 60
    hours = minutes // 60
    second = all_seconds % 60
    return '{}:{:0=2d}:{}'.format(hours, minutes, second)


class Song:
    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_album(self):
        return self.__album

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return in_seconds(self.__length)
        if minutes:
            return (in_seconds(self.__length) // 60)
        if hours:
            return (in_seconds(self.__length) // 3600)

        return self.__length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.get_artist(), self.get_title(), self.get_album(), self.get_length())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.get_artist() == other.get_artist() and \
            self.get_title() == other.get_title() and \
            self.get_album() == other.get_album() and \
            self.get_length() == other.get_length()

    def __hash__(self):
        return hash(self.__str__())

    def prepare_json(self):
        song_dict = {"title": self.__title, "artist": self.__artist, "album": self.__album, "length": self.__length}
        return song_dict


class PlayList:
    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = False
        self.__shuffle = False
        self.__songs = []
        self.__played_songs = []

    def get_name(self):
        return self.__name

    def get_repeat(self):
        return self.__repeat

    def get_shuffle(self):
        return self.__shuffle

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, song):
        try:
            self.__songs.remove(song)
        except ValueError as e:
            pass

    def add_songs(self, songs):
        for song in songs:
            if song not in self.__songs:
                self.add_song(song)

    def total_length(self):
        result = 0

        for song in self.__songs:
            result += in_seconds(song.get_length())

        return seconds_to_string(result)

    def artists(self):
        result = {}

        for song in self.__songs:
            if song.get_artist() not in result:
                result[song.get_artist()] = 1
            else:
                result[song.get_artist()] += 1

        return result

    def next_song(self, repeat=False, shuffle=False):
        if len(self.__songs) == 0:
            return None
        if shuffle:
            current = choice(self.__songs)
        else:
            current = self.__songs[0]

        self.__songs.remove(current)
        self.__played_songs.add(current)

        if repeat and len(self.__songs) == 0:
            self.__songs = self.__played_songs
            self.__played_songs = []

        return current

    def pprint_playlist(self):
        headers = ["Song", "Artist", "Length"]
        table = []

        for song in self.__songs:
            table.append([song.get_title(), song.get_artist(), song.get_length()])

        print(tabulate(table, headers=headers))

    def prepare_json(self):
        result = {
            "name": self.__name,
            "songs": [song.prepare_json() for song in self.__songs],
            "repeat": self.__repeat,
            "shuffle": self.__shuffle
        }

        return result

    def save(self, indent=True):
        filename = self.__name.replace(" ", "-") + ".json"
        filename = os.path.join("playlist-data", filename)

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        filename = os.path.join("playlist-data", filename)

        with open(filename, "r") as f:
            contents = f.read()
            playlist_json = json.loads(contents)
            result = PlayList(playlist_json["name"], repeat=playlist_json["repeat"], shuffle=playlist_json["shuffle"])

            for dict_song in playlist_json["songs"]:
                song = Song(title=dict_song["title"], artist=dict_song["artist"], album=dict_song["album"], length=dict_song["length"])
                result.add_song(song)

            return result


def create_and_save():
    pl1 = PlayList("Ani", repeat=True)
    s1 = Song("Jiva rana", "Slav4o", "Ne pomnq", "4:01")
    s2 = Song("Neka me boli", "Neizvesten", "Nqma", "6:90")
    s3 = Song("Kiofteta", "Peevski", "Koj???", "3:10")
    pl1.add_song(s1)
    pl1.add_songs([s2, s3])
    pl1.pprint_playlist()
    pl1.save(indent=True)


def load():
    new_pl = PlayList.load("Ani.json")
    new_pl.pprint_playlist()


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def get_info(self, data):
        song_data = {}
        try:
            song_data["title"] = data["TIT2"].text[0]
        except:
            song_data["title"] = "Unknown Title"
        try:
            song_data["artist"] = data["TPE1"].text[0]
        except:
            song_data["artist"] = "Unknown Artist"
        try:
            song_data["album"] = data["TALB"].text[0]
        except:
            song_data["album"] = "Unknown Album"
        try:
            song_data["length"] = str(datetime.timedelta(seconds=data.info.length//1))[2:]
        except:
            song_data["length"] = "Unknown"
        return song_data

    def generate_playlist(self, name):
        pl2 = PlayList(name)
        songs = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith(".mp3")]

        for song in songs:
            data = mutagen.File(self.path + "/" + song)
            info = self.get_info(data)
            new_song = Song(title=info["title"], artist=info["artist"], album=info["album"], length=info["length"])
            pl2.add_song(new_song)
        return pl2


def main():
    # load()
    create_and_save()
    crawler = MusicCrawler("/Users/ivan/Downloads")
    new_playlist = crawler.generate_playlist("new_playlist")
    new_playlist.pprint_playlist()


if __name__ == '__main__':
    main()
