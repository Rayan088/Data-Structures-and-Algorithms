class Stats:
    def __init__(self):
        self.total_duration = 0
        self.total_play_count = 0
        self.genre_counts = {}

    #Initialiser method

    def update_total_duration(self, song):
        self.total_duration += song.duration
    
    #Method which adds song duration

    def update_total_play_counts(self):
        self.total_play_count += 1

    #Method which appends play count by 1

    def update_genre_counts(self, song):
        if song.genre in self.genre_counts:
            self.genre_counts[song.genre] += 1
        else:
            self.genre_counts[song.genre] = 1

    #Method which calculates no of songs per genre

    def total_duration_(self):
        return f"Total duration: {self.total_duration}"
    
    #Method which displays total duration
    
    def total_play_counts_(self):
        return f"Total songs played: {self.total_play_count}"
    
    #Method which displays total songs played
    
    def genre_counts_(self):
        genre_summary = "Genre Breakdown: \n"
        for genre, count in self.genre_counts.items():
            genre_summary += (f"{genre}: {count} tracks\n")
        return genre_summary
    
    #Method which displays the genre breakdown