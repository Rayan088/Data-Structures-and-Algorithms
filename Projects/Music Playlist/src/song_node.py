import csv

class SongNode:
    def __init__(self, title, artist, duration, genre, next=None, prev=None):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.next = next
        self.prev = prev
    
    #Initialiser method declaring SongNode attributes

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration})"
    
    #Str method for user friendly representation

    def import_songs(self, csv_file):
        try:
            with open(csv_file, mode="r", newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['Title']
                    artist = row['Artist']
                    duration = row['Duration']
                    genre = row['Genre']
                    self.add_song(title, artist, duration, genre)
            return f"Successfully imported songs from {csv_file}."
        
        except Exception as e:
            return f"Error importing songs: {e}"

    #Method to import songs from csv file