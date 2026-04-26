from src.song_node import SongNode
from src.stats import Stats

import random
import csv

class Playlist:
    def __init__(self, head=None, tail=None, curr=None):
        self.head = head
        self.tail = tail
        self.curr = curr
        self.stats = Stats()

    #Initaliser method

    def add_song(self, title, artist, duration, genre):
        new_node = SongNode(title, artist, duration, genre)

        if self.head is None:
            self.head = self.tail = self.curr = new_node
            self.stats.update_total_duration(new_node)
            self.stats.update_genre_counts(new_node)
            self.stats.update_total_play_counts()
            
            return f"Now playing {self.curr}\n"

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        self.stats.update_total_duration(new_node)

        return f"New song added to end of list (Title: {new_node.title}, Artist: {new_node.artist}, Duration {new_node.duration} seconds, Genre: {new_node.genre})\n"

    #Method which adds song to end of linked list

    def remove_song(self, title):
        if self.head is None:
            return "Playlist is empty. No song to remove.\n"
        
        curr = self.head

        while curr:
            if curr.title == title:
                self.stats.update_genre_counts(curr, remove=True)
                self.stats.update_total_duration(curr, remove=True)

                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None

                elif curr == self.tail:
                    self.tail = curr.prev
                    if self.tail:
                        self.tail.next = None

                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

                if curr == self.curr:
                    if curr.next:
                        self.curr = curr.next
                    else:
                        self.curr = curr.prev

                return f"Song '{title}' has been removed \n"

            curr = curr.next

        return f"Song '{title}' not found in the playlist \n"   

    #Method which removes song

    def prev_song(self):
        if self.curr == None:
            return "Playlist is empty"

        if self.curr and self.curr.prev:
            self.curr = self.curr.prev
            return f"Now playing {self.curr}\n"
        
        return f"Already at the start of the playlist\n"

    #Method which moves to previous song

    def next_song(self):
        if self.curr == None:
            return "Playlist is empty"
        
        if self.curr and self.curr.next:
            self.curr = self.curr.next
            self.stats.update_total_play_counts()
            return f"Now playing {self.curr}\n"

        return f"Already at the end of the playlist\n"
        
    #Method which moves to next song

    def shuffle(self):
        curr = self.head

        if curr is None:
            return "Playlist is empty\n"
        
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
        return f"Playlist has been shuffled! Now playing {self.curr}\n"

    #Method which shuffles songs

    def import_songs(self, csv_file):
        try:
            with open(csv_file, newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)

                next(reader)  # skip header row

                count = 0
                for row in reader:
                    title = row[0]
                    artist = row[1]
                    duration = int(row[2])
                    genre = row[3]

                    self.add_song(title, artist, duration, genre)
                    count += 1

                return f"{count} songs imported successfully!\n"

        except FileNotFoundError:
            return "File not found.\n"

        except Exception as e:
            return f"An error occurred: {e}\n"
            
    #Method which adds songs from csv file