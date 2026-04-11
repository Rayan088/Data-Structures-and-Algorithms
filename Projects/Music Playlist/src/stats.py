from playlist import Playlist

class Stats:
    def __init__(self):
        self.total_duration = 0
        self.total_play_count = 0
        self.genre_counts = {}

    def update_total_duration(self, song):
        self.total_duration += song.duration

    def update_total_play_counts(self):
        self.total_play_count += 1
        return f"Total songs played: {self.total_play_count}"

    def update_genre_counts(self, song):
        if song.genre in self.genre_counts:
            self.genre_counts[song.genre] += 1
        else:
            self.genre_counts[song.genre] = 1

    def total_duration_(self):
        return f"Total duration: {self.total_duration}"
    
    def total_play_counts_(self):
        return f"Total songs played: {self.total_play_count}"
    
    def genre_counts_(self):
        genre_summary = "Genre Breakdown: \n"
        for genre, count in self.genre_counts.items():
            genre_summary += (f"{genre}: {count} tracks")
        return genre_summary