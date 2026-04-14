from playlist import Playlist
from stats import Stats

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
                   "7. Import Songs from CSV\n"
                   "8. Exit\n")
        
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
            file_name = "Projects/Music_Playlist/data/songs.csv"
            print(pl.import_songs(file_name))

        elif choice == "8":
            print("Exited playlist\n")
            break

        else:
            print("Invalid input entered\n")

#Main function of user menu

if __name__ == "__main__":
    main()