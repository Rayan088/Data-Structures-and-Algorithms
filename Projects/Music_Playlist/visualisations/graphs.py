import matplotlib.pyplot as plt
import seaborn as sns

class Graphs:
    def __init__(self, playlist):
        self.playlist = playlist

    #Initialiser method

    def get_all_songs(self):
        songs = []
        curr = self.playlist.head

        while curr:
            songs.append(curr)
            curr = curr.next

        return songs

    #Method which extracts all songs

    def song_durations(self):
        songs = self.get_all_songs()

        durations = []
        for song in songs:
            durations.append(song.duration)

        bins = {
            "0-120s": 0,
            "120-180s": 0,
            "180-240s": 0,
            "240+": 0
        }

        for d in durations:
            if d <= 120:
                bins["0-120s"] += 1
            elif d <=180:
                bins["120-180s"] += 1
            elif d <= 240:
                bins["180-240s"] += 1
            else:
                bins["240+"] += 1

    def songs_per_genre(self):
        songs = self.get_all_songs()

        all_genres = {}

        for song in songs:
            if song.genre in all_genres:
                all_genres[song.genre] += 1
            else:
                all_genres[song.genre] = 1

    def common_title_words(self):
        songs = self.get_all_songs()

        most_common_words = {}
        for song in songs:
            words = song.title.split()

            for word in words:
                word = word.lower()

                if word in songs:
                    most_common_words[word] += 1
                else:
                    most_common_words[word] = 1