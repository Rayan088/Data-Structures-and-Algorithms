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
        tk.Button(self.main_frame, text="Add Song", command=self.add_song).pack()
        tk.Button(self.main_frame, text="Remove Song", command=self.remove_song).pack()
        tk.Button(self.main_frame, text="Next Song", command=self.next_song).pack()
        tk.Button(self.main_frame, text="Previous Song", command=self.previous_song).pack()
        tk.Button(self.main_frame, text="Shuffle", command=self.shuffle).pack()
        tk.Button(self.main_frame, text="Import CSV", command=self.import_from_csv).pack()

        tk.Button(self.main_frame, text="Stats", command=self.stats).pack()
        tk.Button(self.main_frame, text="Visualisation", command=self.visualisations).pack()

    def create_stats_frame(self):
        pass

    def create_graphs_frame(self):
        pass

    def add_song(self, song):
        pass

    def remove_song(self, song):
        pass

    def next_song(self):
        pass

    def previous_song(self):
        pass

    def shuffle(self):
        pass

    def import_from_csv(self):
        pass

    def stats(self):
        pass

    def visualisations(self):
        pass

root = tk.Tk()
app = App(root)
root.mainloop()