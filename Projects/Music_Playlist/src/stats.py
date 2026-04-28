class Stats:
    def __init__(self):
        self.total_duration = 0
        self.total_play_count = 0
        self.genre_counts = {}
        self.artist_counts = {}

    #Initialiser method

    def total_duration(self, song, remove=False):
        if remove:
            self.total_duration -= song.duration
        else:
            self.total_duration += song.duration

        return f"Total duration: {self.total_duration} seconds"
    
    #Method which adds song duration

    def total_play_counts(self, remove=False):
        if remove:
            self.total_play_count -= 1
        else:
            self.total_play_count += 1

        return f"Total songs played: {self.total_play_count}"

    #Method which appends play count by 1

    def max_genre_count(self, song, remove=False):
        if remove:
            if song.genre in self.genre_counts:
                self.genre_counts[song.genre] -= 1
                if self.genre_counts[song.genre] == 0:
                    del self.genre_counts[song.genre]

        else:
            if song.genre in self.genre_counts:
                self.genre_counts[song.genre] += 1
            else:
                self.genre_counts[song.genre] = 1

        max_count = 0
        max_genre = None
        max_index = -1

        for i, (genre, count) in enumerate(self.genre_counts.items()):
            if count > max_count:
                max_count = count
                max_genre = genre
                max_index = i

            return max_index, max_genre, max_count

    #Method which calculates max no of songs per genre

    def max_artist_count(self, song, remove=False):
        if remove:
            if song in self.artist_counts:
                self.artist_counts[song.artist] -= 1
                if self.artist_counts[song.artist] == 0:
                    del self.genre_counts[song.genre]
        
        else:
            if song.artist in self.artist_counts:
                self.artist_counts[song.artist] += 1
            else:
                self.artist_counts[song.artist] = 1

        max_count = 0
        max_artist = None
        max_index = -1

        for i, (artist, count) in enumerate(self.artist_counts.items()):
            if count > max_count:
                max_count = count
                max_artist = artist
                max_index = i

        return max_index, max_artist, max_count           

    #Method which calculates max no of songs by an artist