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
        tk.Label(self.stats_frame, text="Stats").pack()

    def create_graphs_frame(self):
        tk.Label(self.graph_frame, text="Visualisations").pack()

    def add_song(self):
        if not hasattr(self, "popup"):
            self.popup = tk.Toplevel(self.root)
            self.popup.title("Add Song")
            self.popup.geometry("300x300")

            tk.Label(self.popup, text="Title").grid(row=0, column=0, padx=5, pady=5)
            self.title_entry = tk.Entry(self.popup)
            self.title_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(self.popup, text="Artist").grid(row=1, column=0, padx=5, pady=5)
            self.artist_entry = tk.Entry(self.popup)
            self.artist_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(self.popup, text="Duration").grid(row=2, column=0, padx=5, pady=5)
            self.duration_entry = tk.Entry(self.popup)
            self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(self.popup, text="Genre").grid(row=3, column=0, padx=5, pady=5)
            self.genre_entry = tk.Entry(self.popup)
            self.genre_entry.grid(row=3, column=1, padx=5, pady=5)

            tk.Button(self.popup, text="Add Song", command=self.add_song).grid(row=4, column=0, columnspan=2, pady=10)

        else:
            title = self.title_entry.get()
            artist = self.artist_entry.get()

            try:
                duration = int(self.duration_entry.get())
            except:
                messagebox.showerror("Error", "Duration must be a number")
                return

            genre = self.genre_entry.get()

            self.pl.add_song(title, artist, duration, genre)
            messagebox.showinfo("Success", "Song added")

            self.popup.destroy()
            del self.popup

    def remove_song(self):
        if not hasattr(self, "remove_popup"):
            self.remove_popup = tk.Toplevel(self.root)
            self.remove_popup.title("Remove Song")
            self.remove_popup.geometry("300x300")

            tk.Label(self.remove_popup, text="Enter song title").grid(row=0, column=0, padx=5, pady=5)

            self.remove_entry = tk.Entry(self.remove_popup)
            self.remove_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Button(self.remove_popup, text="Remove Song", command=self.remove_song).grid(row=1, column=1, sticky="w", columnspan=2, pady=0)

        else:
            remove_title = self.remove_entry.get()
            if remove_title == "":
                messagebox.showerror("Error", "Enter a song title")
                return
            
            self.pl.remove_song(remove_title)
            messagebox.showinfo("Success", "Song removed")

            self.remove_popup.destroy()
            del self.remove_popup

    def next_song(self):
        self.pl.next_song()

    def previous_song(self):
        self.pl.prev_song()

    def shuffle(self):
        self.pl.shuffle()

    def import_from_csv(self):
        self.pl.import_songs("data/songs.csv")

    def stats(self):
        self.show_frame(self.stats_frame)

    def visualisations(self):
        self.show_frame(self.graph_frame)

root = tk.Tk()
app = App(root)
root.mainloop()