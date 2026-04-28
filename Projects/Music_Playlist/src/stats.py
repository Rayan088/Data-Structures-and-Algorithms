class Stats:
    def __init__(self):
        self.total_duration = 0
        self.total_play_count = 0
        #self.genre_counts = {}
        self.artist_counts = {}

    #Initialiser method

    def total_duration_(self, playlist):
        total = 0
        curr = playlist.head

        while curr:
            total += curr.duration
            curr = curr.next

        hours = total // 3600
        remaining_seconds = total % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        return f"{hours}h {minutes}m {seconds}s"
    
    #Method which adds song duration

    def total_play_counts_(self, remove=False):
        if remove:
            self.total_play_count -= 1
        else:
            self.total_play_count += 1

        return f"Total songs played: {self.total_play_count}"

    #Method which appends play count by 1

    def max_genre_count_(self, playlist):
        genre_counts = {}
        curr = playlist.head

        while curr:
            genre = curr.genre

            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1
            
            curr = curr.next

        max_genre = None
        max_genre_count = 0

        for genre, count in genre_counts.items():
            if count > max_genre_count:
                max_genre_count = count
                max_genre = genre

        return max_genre, max_genre_count

    #Method which calculates max no of songs per genre

    def max_artist_count(self, song, remove=False):
        if remove:
            if song in self.artist_counts:
                self.artist_counts[song.artist] -= 1
                if self.artist_counts[song.artist] == 0:
                    del self.artist_counts[song.artist]
        
        else:
            if song.artist in self.artist_counts:
                self.artist_counts[song.artist] += 1
            else:
                self.artist_counts[song.artist] = 1

        max_artist_count = 0
        max_artist = None
        max_index = -1

        for i, (artist, count) in enumerate(self.artist_counts.items()):
            if count > max_artist_count:
                max_artist_count = count
                max_artist = artist
                max_index = i

        return max_index, max_artist, max_artist_count           

    #Method which calculates max no of songs by an artist