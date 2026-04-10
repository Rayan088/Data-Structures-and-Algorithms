from song_node import SongNode

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
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    #Method which adds song to end of linked list

    def remove_song(self):
        pass

    #Method which removes song

    def prev_song(self):
        if self.curr and self.curr.prev:
            self.curr = self.curr.prev
        else:
            print("Already at the start of the playlist")

    #Method which moves to previous song

    def next_song(self):
        if self.curr and self.curr.next:
            self.curr = self.curr.next
        else:
            print("Already at the end of the playlist")
        
    #Method which moves to next song

    def shuffle(self):
        pass

    #Method which shuffles songs