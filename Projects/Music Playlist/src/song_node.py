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