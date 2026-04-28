class Stats:
    #def __init__(self):
        #self.total_duration = 0
        #self.total_play_count = 0
        #self.genre_counts = {}
        #self.artist_counts = {}

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

    def total_play_counts_(self, playlist):
        song_count = 0
        curr = playlist.head

        while curr:
            song_count += 1
            curr = curr.next

        return song_count

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

    def max_artist_count(self, playlist):
        artist_counts = {}
        curr = playlist.head

        while curr:
            artist = curr.artist

            if artist in artist_counts:
                artist_counts[artist] += 1
            else:
                artist_counts[artist] = 1
            
            curr = curr.next

        max_artist = None
        max_artist_count = 0

        for artist, count in artist_counts.items():
            if count > max_artist_count:
                max_artist_count = count
                max_artist = artist

        return max_artist, max_artist_count

    #Method which calculates max no of songs by an artist