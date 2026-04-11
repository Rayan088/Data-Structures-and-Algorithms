from playlist import Playlist

class Statistics:
    def __init__(self):
        self.total_duration = 0
        self.total_play_count = 0
        self.genre_counts = {}

    def total_duration(self, song):
        self.total_duration += song.duration
        return f"Total duration: {self.total_duration}"

    def total_play_counts(self):
        self.total_play_count += 1
        return f"Total songs played: {self.total_play_count}"

    def genre_counts(self, song):
        if song.genre in self.genre_counts:
            self.genre_counts[self.genre] += 1
        else:
            self.genre_counts[self.genre] = 1
        
        for genre, count in self.genre_counts.items():
            print(f"{genre}: {count} tracks")