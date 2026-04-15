from playlist import Playlist
from visualisations.graphs import Graphs

def stats_menu(pl):
    st = pl.stats

    while True:

        choice = input("--- Stats Menu --- \n"
                       "1. Total Duration\n"
                       "2. Total Play Counts\n"
                       "3. Genre Counts\n"
                       "4. Exit\n")
        
        if choice == "1":
            print(st.total_duration_())

        elif choice == "2":
            print(st.total_play_counts_())
        
        elif choice == "3":
            print(st.genre_counts_())

        elif choice == "4":
            print("Exited stats")
            break
        
        else:
            print("Invalid input entered")

#Method which displays user menu for stats

def graphs_menu(pl):
    graphs_ = Graphs(pl)

    while True:
        
        choice = input("---Visualisations--- \n"
                       "1. Songs per Duration \n"
                       "2. Songs per Genre \n"
                       "3. Most common title words \n"
                       "4. Exit \n")
        
        if choice == "1":
            graphs_.song_durations()

        elif choice == "2":
            graphs_.songs_per_genre()

        elif choice == "3":
            graphs_.common_title_words()

        elif choice == "4":
            print("Exited visualisations")
            break

        else:
            print("Invalid input entered")

#Method which displays user menu for visualisations

def main():
    pl = Playlist()
    
    while True:
        choice = input("--- Playlist Menu ---\n"
                   "1. Add Song\n"
                   "2. Remove Song\n"
                   "3. Next Song\n"
                   "4. Previous Song\n"
                   "5. Shuffle\n"
                   "6. Stats\n"
                   "7. Visualisations\n"
                   "8. Import Songs from CSV\n"
                   "9. Exit\n")
        
        if choice == "1":
            title = input("Title: ")
            artist = input("Artist: ")
            duration = input("Duration (in seconds): ")
            genre = input("Genre: ")

            print(pl.add_song(title, artist, duration, genre))
        
        elif choice == "2":
            print(pl.remove_song())

        elif choice == "3":
            print(pl.next_song())

        elif choice == "4":
            print(pl.prev_song())

        elif choice == "5":
            print(pl.shuffle())

        elif choice == "6":
            stats_menu(pl)

        elif choice == "7":
            graphs_menu(pl)

        elif choice == "8":
            file_name = "Projects/Music_Playlist/data/songs.csv"
            print(pl.import_songs(file_name))

        elif choice == "9":
            print("Exited playlist\n")
            break

        else:
            print("Invalid input entered\n")

#Main function of user menu

if __name__ == "__main__":
    main()