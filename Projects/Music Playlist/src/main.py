from playlist import Playlist

def main():
    pl = Playlist()
    
    while True:
        choice = input("--- Playlist Menu ---\n"
                   "1. Add Song\n"
                   "2. Remove Song\n"
                   "3. Next Song\n"
                   "4. Previous Song\n"
                   "5. Shuffle\n"
                   "6. Exit\n")
        
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
            print("Exited playlist\n")
            break

        else:
            print("Invalid input entered\n")

if __name__ == "__main__":
    main()