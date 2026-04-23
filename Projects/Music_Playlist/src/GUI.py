import tkinter as tk
import tkinter.messagebox as messagebox

from src.playlist import Playlist
from visualisations.graphs import Graphs

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Music Playlist")

        self.pl = Playlist()
        self.graphs = Graphs(self.pl)

        self.main_frame = tk.Frame(root)
        self.stats_frame = tk.Frame(root)
        self.graph_frame = tk.Frame(root)

        self.create_main_frame()
        self.create_stats_frame()
        self.create_graphs_frame()

        self.show_frame(self.main_frame)

    def show_frame(self, frame):
        for f in (self.main_frame, self.stats_frame, self.graph_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    def create_main_frame(self):
        tk.Label(self.main_frame, text="Title").pack()
        self.title_entry = tk.Entry(self.main_frame)
        self.title_entry.pack()

        tk.Label(self.main_frame, text="Artist").pack()
        self.artist_entry = tk.Entry(self.main_frame)
        self.artist_entry.pack()

        tk.Label(self.main_frame, text="Duration").pack()
        self.duration_entry = tk.Entry(self.main_frame)
        self.duration_entry.pack()

        tk.Label(self.main_frame, text="Genre").pack()
        self.genre_entry = tk.Entry(self.main_frame)
        self.genre_entry.pack()

        tk.Label(self.main_frame, text="Remove Title").pack()
        self.remove_entry = tk.Entry(self.main_frame)
        self.remove_entry.pack()

        tk.Button(self.main_frame, text="Add Song", command=self.add_song).pack()
        tk.Button(self.main_frame, text="Remove Song", command=self.remove_song).pack()
        tk.Button(self.main_frame, text="Next Song", command=self.next_song).pack()
        tk.Button(self.main_frame, text="Previous Song", command=self.previous_song).pack()
        tk.Button(self.main_frame, text="Shuffle", command=self.shuffle).pack()
        tk.Button(self.main_frame, text="Import CSV", command=self.import_from_csv).pack()

        tk.Button(self.main_frame, text="Stats", command=self.stats).pack()
        tk.Button(self.main_frame, text="Visualisation", command=self.visualisations).pack()

    def create_stats_frame(self):
        tk.Label(self.stats_frame, text="Stats").pack()

    def create_graphs_frame(self):
        tk.Label(self.graph_frame, text="Visualisations").pack()

    def add_song(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()

        try:
            duration = int(self.duration_entry.get())
        except:
            return

        genre = self.genre_entry.get()

        self.pl.add_song(title, artist, duration, genre)

    def remove_song(self):
        remove_title = self.remove_entry.get()
        self.pl.remove_song(remove_title)

    def next_song(self):
        self.pl.next_song()

    def previous_song(self):
        self.pl.prev_song()

    def shuffle(self):
        self.pl.shuffle()

    def import_from_csv(self):
        self.import_from_csv()

    def stats(self):
        self.show_frame(self.stats_frame)

    def visualisations(self):
        self.show_frame(self.graph_frame)

root = tk.Tk()
app = App(root)
root.mainloop()