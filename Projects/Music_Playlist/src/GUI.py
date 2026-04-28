import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from src.playlist import Playlist
from visualisations.graphs import Graphs
from src.stats import Stats

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Music Playlist")
        self.root.configure(bg="lightblue")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.pl = Playlist()
        self.stats = Stats()
        self.graphs = Graphs(self.pl)

        self.main_frame = tk.Frame(root)
        self.stats_frame = tk.Frame(root)
        self.graph_frame = tk.Frame(root)

        self.create_main_frame()
        self.create_graphs_frame()

        self.show_frame(self.main_frame)

    def on_close(self):
        plt.close("all")
        self.root.quit()
        self.root.destroy()

    def show_frame(self, frame):
        for f in (self.main_frame, self.stats_frame, self.graph_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="#120A38")

        for i in range(8):
            if i in (0, 7):
                self.main_frame.columnconfigure(i, weight=1)
            else:
                self.main_frame.columnconfigure(i, weight=0)

        tk.Label(self.main_frame, text="Music Playlist", font=("Arial", 28, "bold"), bg="#120A38", fg="#FFFFFF").grid(row=0, column=1, columnspan=6, pady=10)
        tk.Label(self.main_frame, text="Manage and enjoy your favourite songs", font=("Arial", 12), bg="#120A38", fg="#FFFFFF").grid(row=1, column=1, columnspan=6)

        tk.Button(self.main_frame, text="Add Song", command=self.add_song, bg="#22145C", fg="#FFFFFF").grid(row=2, column=1, padx=15, pady=50)
        tk.Button(self.main_frame, text="Remove Song", command=self.remove_song, bg="#22145C", fg="#FFFFFF").grid(row=2, column=2, padx=15, pady=50)
        tk.Button(self.main_frame, text="Next Song", command=self.next_song, bg="#22145C", fg="#FFFFFF").grid(row=2, column=3, padx=15, pady=50)
        tk.Button(self.main_frame, text="Previous Song", command=self.previous_song, bg="#22145C", fg="#FFFFFF").grid(row=2, column=4, padx=15, pady=50)
        tk.Button(self.main_frame, text="Shuffle", command=self.shuffle, bg="#22145C", fg="#FFFFFF").grid(row=2, column=5, padx=15, pady=50)
        tk.Button(self.main_frame, text="Import CSV", command=self.import_from_csv, bg="#22145C", fg="#FFFFFF").grid(row=2, column=6, padx=15, pady=50)

        tk.Button(self.main_frame, text="Stats", command=self.show_stats, bg="#22145C", fg="#FFFFFF").grid(row=3, column=3, padx=15, pady=20)
        tk.Button(self.main_frame, text="Visualisation", command=self.visualisations, bg="#22145C", fg="#FFFFFF").grid(row=3, column=4, padx=15, pady=20)

        self.result_label = tk.Label(self.main_frame, text="Welcome to the playlist manager",
                                     font=("Arial", 14), bg="#1A1248", fg="#FFFFFF", width=70, height=8,
                                      wraplength=1000, justify="left", anchor="nw", relief="solid",
                                      bd=2, highlightbackground="#6D28D9", highlightthickness=2)
        
        self.result_label.grid(row=4, column=1, columnspan=6, pady=30)

    def create_stats_frame(self):
        self.stats_frame = tk.Frame(self.root, bg="#120A38")

        for i in range(6):
            self.stats_frame.grid_columnconfigure(i, weight=1)

        tk.Label(self.stats_frame, text="Statistics", font=("Arial", 28, "bold"), bg="#120A38", fg="#FFFFFF").grid(row=0, column=0, columnspan=6, pady=10, sticky="nsew")   
        tk.Label(self.stats_frame, text="Key Metrics and Insights", font=("Arial", 12), bg="#120A38", fg="#FFFFFF").grid(row=1, column=0, columnspan=6)

        total_duration = self.stats.total_duration_(self.pl)
        box1 = tk.Frame(self.stats_frame, bg="#1a1040", highlightbackground="#4a3080", highlightthickness=1, width=400, height=225)
        box1.grid(row=2, column=2, padx=14, pady=14, sticky="nsew")
        box1.grid_propagate(False)
        tk.Label(box1, text="TOTAL DURATION", font=("Arial", 10, "bold"), bg="#1a1040", fg="#a899cc").grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        tk.Label(box1, text=total_duration, font=("Arial", 22, "bold"), bg="#1a1040", fg="#FFFFFF").grid(row=3, column=0, padx=20,             sticky="w")
        tk.Label(box1, text="of music in your playlist", font=("Arial", 9), bg="#1a1040", fg="#a899cc").grid(row=4, column=0, padx=20, pady=(0,10), sticky="w")

        song_count = self.stats.total_play_counts_(self.pl)
        box2 = tk.Frame(self.stats_frame, bg="#1a1040", highlightbackground="#4a3080", highlightthickness=1, width=400, height=225)
        box2.grid(row=2, column=3, padx=14, pady=14, sticky="nsew")
        box2.grid_propagate(False)
        tk.Label(box2, text="TOTAL PLAY COUNTS", font=("Arial", 10, "bold"), bg="#1a1040", fg="#a899cc").grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        tk.Label(box2, text=song_count, font=("Arial", 22, "bold"), bg="#1a1040", fg="#FFFFFF").grid(row=3, column=0, padx=20, sticky="w")
        tk.Label(box2, text="total songs", font=("Arial", 9), bg="#1a1040", fg="#a899cc").grid(row=4, column=0, padx=20, pady=(0,10), sticky="w")

        max_genre, max_genre_count = self.stats.max_genre_count_(self.pl)
        box3 = tk.Frame(self.stats_frame, bg="#1a1040", highlightbackground="#4a3080", highlightthickness=1, width=400, height=225)
        box3.grid(row=3, column=2, padx=14, pady=14, sticky="nsew")
        box3.grid_propagate(False)
        tk.Label(box3, text="MAX GENRE COUNT", font=("Arial", 10, "bold"), bg="#1a1040", fg="#a899cc").grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        tk.Label(box3, text=max_genre_count, font=("Arial", 22, "bold"), bg="#1a1040", fg="#FFFFFF").grid(row=3, column=0, padx=20, sticky="w")
        tk.Label(box3, text=max_genre, font=("Arial", 9), bg="#1a1040", fg="#9b6bff").grid(row=4, column=0, padx=20, pady=(0,10), sticky="w")

        max_artist, max_artist_count = self.stats.max_artist_count(self.pl)
        box4 = tk.Frame(self.stats_frame, bg="#1a1040", highlightbackground="#4a3080", highlightthickness=1, width=400, height=225)
        box4.grid(row=3, column=3, padx=14, pady=14, sticky="nsew")
        box4.grid_propagate(False)
        tk.Label(box4, text="MAX ARTIST COUNT", font=("Arial", 10, "bold"), bg="#1a1040", fg="#a899cc").grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        tk.Label(box4, text=max_artist_count, font=("Arial", 22, "bold"), bg="#1a1040", fg="#FFFFFF").grid(row=3, column=0, padx=20, sticky="w")
        tk.Label(box4, text=max_artist, font=("Arial", 9), bg="#1a1040", fg="#9b6bff").grid(row=4, column=0, padx=20, pady=(0, 10), sticky="w")
            
        tk.Button(self.stats_frame, text="Back to Home", command=lambda: self.show_frame(self.main_frame), bg="#22145C", fg="#FFFFFF").grid(row=4, column=0, columnspan=6, pady=50)

    def create_graphs_frame(self):
        self.graph_frame = tk.Frame(self.root, bg="#120A38")

        for i in range(6):
            self.graph_frame.grid_columnconfigure(i, weight=1)

        self.graph_frame.grid_rowconfigure(2, weight=1)

        tk.Label(self.graph_frame, text="Visualisations", font=("Arial", 28, "bold"), bg="#120A38", fg="#FFFFFF").grid(row=0, column=0, columnspan=6, pady=10, sticky="snew")
        tk.Label(self.graph_frame, text="Explore your playlist insights and trends", font=("Arial", 12), bg="#120A38", fg="#FFFFFF").grid(row=1, column=0, columnspan=6)

        style = ttk.Style()
        style.theme_use("default")

        style.configure("TNotebook", background="#120A38", borderwidth=0)
        style.configure("TNotebook.Tab", background="#22145C", foreground="white", padding=[20, 10])
        style.map("TNotebook.Tab", background=[("selected", "#6D28D9")], foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(self.graph_frame)
        self.notebook.grid(row=2, column=0, columnspan=6, padx=20, pady=10, sticky="nsew")

        self.tab1 = tk.Frame(self.notebook, bg="#120A38")
        self.tab2 = tk.Frame(self.notebook, bg="#120A38")
        self.tab3 = tk.Frame(self.notebook, bg="#120A38")

        self.notebook.add(self.tab1, text="Duration")
        self.notebook.add(self.tab2, text="Genre")
        self.notebook.add(self.tab3, text="Title Words")

        for tab in (self.tab1, self.tab2, self.tab3):
            tab.grid_rowconfigure(0, weight=1)
            tab.grid_columnconfigure(0, weight=1)

        tk.Button(self.graph_frame, text="Back to Home", command=lambda: self.show_frame(self.main_frame), bg="#22145C", fg="#FFFFFF").grid(row=3, column=0, columnspan=6, pady=50)

    def load_graphs(self):
        for tab in [self.tab1, self.tab2, self.tab3]:
            for widget in tab.winfo_children():
                widget.destroy()

        fig1 = self.graphs.song_durations()
        fig2 = self.graphs.songs_per_genre()
        fig3 = self.graphs.common_title_words()

        canvas1 = FigureCanvasTkAgg(fig1, master=self.tab1)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        canvas2 = FigureCanvasTkAgg(fig2, master=self.tab2)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        canvas3 = FigureCanvasTkAgg(fig3, master=self.tab3)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def add_song(self):
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

        tk.Button(self.popup, text="Add Song", command=self.confirm_add_song).grid(row=4, column=0, columnspan=2, pady=10)

    def confirm_add_song(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        duration = self.duration_entry.get()

        genre = self.genre_entry.get()

        if not (title and artist and duration and genre):
            messagebox.showerror("Error", "Missing Field")
            return
        
        try:
            duration = int(duration)
        except ValueError:
            messagebox.showerror("Error", "Duration must be a number")
            return
        
        message = self.pl.add_song(title, artist, duration, genre)
        self.result_label.config(text=message)
        messagebox.showinfo("Success", message)

        self.popup.destroy()
        del self.popup

    def remove_song(self):
        self.remove_popup = tk.Toplevel(self.root)
        self.remove_popup.title("Remove Song")
        self.remove_popup.geometry("300x300")

        tk.Label(self.remove_popup, text="Enter song title").grid(row=0, column=0, padx=5, pady=5)

        self.remove_entry = tk.Entry(self.remove_popup)
        self.remove_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.remove_popup, text="Remove Song", command=self.confirm_remove_song).grid(row=1, column=1, sticky="w", columnspan=2, pady=0)

    def confirm_remove_song(self):
        remove_title = self.remove_entry.get()

        if remove_title == "":
            messagebox.showerror("Error", "No song title entered")
            return
        
        message = self.pl.remove_song(remove_title)
        self.result_label.config(text=message)
        messagebox.showinfo("Success", message)

        self.remove_popup.destroy()
        del self.remove_popup

    def next_song(self):
        message = self.pl.next_song()
        self.result_label.config(text=message)
        messagebox.showinfo("Now playing", message)

    def previous_song(self):
        message = self.pl.prev_song()
        self.result_label.config(text=message)
        messagebox.showinfo("Now playing", message)

    def shuffle(self):
        message = self.pl.shuffle()
        self.result_label.config(text=message)
        messagebox.showinfo("Now playing", message)

    def import_from_csv(self):
        message = self.pl.import_songs("data/songs.csv")
        self.result_label.config(text=message)
        messagebox.showinfo("Now playing", message)

    def show_stats(self):
        self.create_stats_frame()
        self.show_frame(self.stats_frame)

    def visualisations(self):
        self.load_graphs()
        self.show_frame(self.graph_frame)

root = tk.Tk()
app = App(root)
root.mainloop()