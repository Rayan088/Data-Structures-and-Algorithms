from song_node import SongNode

import random

class Playlist:
    def __init__(self, head=None, tail=None, curr=None):
        self.head = head
        self.tail = tail
        self.curr = curr

    #Initaliser method

    def add_song(self, title, artist, duration, genre):
        new_node = SongNode(title, artist, duration, genre)

        if self.head is None:
            self.head = self.tail = self.curr = new_node
            return f"Now playing {self.curr}"

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return f"New song added to end of list (Title: {new_node.title}, Artist: {new_node.artist}, Duration {new_node.duration} seconds, Genre: {new_node.genre})"

    #Method which adds song to end of linked list

    def remove_song(self):
        pass

    #Method which removes song

    def prev_song(self):
        if self.curr and self.curr.prev:
            self.curr = self.curr.prev
            return f"Now playing {self.curr}"
        return f"Already at the start of the playlist"

    #Method which moves to previous song

    def next_song(self):
        if self.curr and self.curr.next:
            self.curr = self.curr.next
            return f"Now playing {self.curr}"
        return f"Already at the end of the playlist"
        
    #Method which moves to next song

    def shuffle(self):
        curr = self.head

        if curr is None:
            return "Platlist is empty"
        
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        random.shuffle(nodes)

        self.head = nodes[0]
        self.head.prev = None

        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
            nodes[i].prev = nodes[i-1]

        self.tail = nodes[len(nodes) - 1]
        self.tail.next = None
        
        self.curr = self.head
        return f"Playlist has been shuffled! Now playing {self.curr}"

    #Method which shuffles songs


pl = Playlist()

print(pl.add_song("Blinding Lights", "The Weeknd", 200, "Pop"))
print(pl.add_song("Bohemian Rhapsody", "Queen", 354, "Rock"))
print(pl.add_song("Shape of You", "Ed Sheeran", 240, "Pop"))
print(pl.add_song("Lose Yourself", "Eminem", 326, "Hip-Hop"))
print(pl.shuffle())
print(pl.next_song())