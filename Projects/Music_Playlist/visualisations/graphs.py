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
        plt.close("all")

        songs = self.get_all_songs()

        durations = []
        for song in songs:
            durations.append(song.duration)

        bins = {
            "0-120": 0,
            "120-180": 0,
            "180-240": 0,
            "240+": 0
        }

        for d in durations:
            if d <= 120:
                bins["0-120"] += 1
            elif d <=180:
                bins["120-180"] += 1
            elif d <= 240:
                bins["180-240"] += 1
            else:
                bins["240+"] += 1

        labels = list(bins.keys())
        counts = list(bins.values())
        
        sns.set_style("whitegrid")

        fig, ax = plt.subplots(figsize=(6, 3))

        fig.patch.set_facecolor("#120A38")
        ax.set_facecolor("#120A38")

        sns.barplot(x=labels, y=counts, ax=ax, color="#6D28D9", saturation=1)

        ax.set_title("Song Duration Distribution", color="#6D28D9")
        ax.set_xlabel("Duration Range (seconds)", color="white")
        ax.set_ylabel("Number of songs", color="white")

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        return fig

    #Method which generates bar graph of song durations
        
    def songs_per_genre(self):
        plt.close("all")

        songs = self.get_all_songs()

        all_genres = {}

        for song in songs:
            if song.genre in all_genres:
                all_genres[song.genre] += 1
            else:
                all_genres[song.genre] = 1

        labels = list(all_genres.keys())
        counts = list(all_genres.values())

        sns.set_style("whitegrid")

        fig, ax = plt.subplots(figsize=(6, 3))

        fig.patch.set_facecolor("#120A38")
        ax.set_facecolor("#120A38")

        sns.barplot(x=labels, y=counts, ax=ax, color="#6D28D9", saturation=1)

        ax.set_title("Songs Genre Distribution", color="#6D28D9")
        ax.set_xlabel("Genre", color="white")
        ax.set_ylabel("Number of songs", color="white")

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        return fig

    #Method which generates bar graph of song genre quantities

    def common_title_words(self):
        plt.close("all")
        
        songs = self.get_all_songs()

        stop_words =  ["the", "a", "and", "of", "to", "in"]

        most_common_words = {}
        for song in songs:
            for word in song.title.lower().split():
                if word in stop_words:
                    continue
                
                if word in most_common_words:
                    most_common_words[word] += 1
                else:
                    most_common_words[word] = 1

        top_words = dict(sorted(most_common_words.items(), key=lambda x:x[1], reverse=True)[:5])
        #Sorting the list to find top 5 most mentioned words

        labels = list(top_words.keys())
        counts = list(top_words.values())

        sns.set_style("whitegrid")

        fig, ax = plt.subplots(figsize=(6, 3))

        fig.patch.set_facecolor("#120A38")
        ax.set_facecolor("#120A38")

        sns.barplot(x=labels, y=counts, ax=ax, color="#6D28D9", saturation=1)

        ax.set_title("Most Common Title Words", color="#6D28D9")
        ax.set_xlabel("Title Words", color="white")
        ax.set_ylabel("Frequency", color="white")

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        
        return fig

    #Method which generates bar graph of most common title words