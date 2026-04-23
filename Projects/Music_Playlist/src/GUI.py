import tkinter as tk
import tkinter.messagebox as messagebox

from src.playlist import Playlist
from visualisations.graphs import Graphs

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Music Playlist")

        self.main_frame = tk.Frame(root)
        self.stats_frame = tk.Frame(root)
        self.graph_frame = tk.Frame(root)

        self.show_frame()

    def show_frame(self, frame):
        for f in (self.main_frame, self.stats_frame, self.graph_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

root = tk.Tk()
app = App(root)
root.mainloop()