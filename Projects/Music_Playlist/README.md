### Overview

A python based music playlist tool that allows users to manage and interact with their music collection by playlist navigation, song management, shuffle functionality, statistical analysis, data visualisation and CSV-based improrting implemented through linked list data structures.

### Features

- Add and remove songs from a playlist
- Navigate between songs (next, previous)
- Shuffle the playlist randomly
- Track playlist statistics (Total duration, playcount, genre distribution)
- Generate visualisations (Song duration distribution, songs per genre, most common words in song titles)
- Import ready made playlist from a CSV file

### Data Structures & Concepts

- Doubly linked list for playlist management
- Data analysis (stats tracking)
- Data visualisation using matplotlib and seaborn
- File handling with CSV import

### How to Run

Project requres python installed (preferred: python 3.13)

Install Dependences:  
pip install matplotlib seaborn

Run program using:  
python.main.py

Make sure your entered files exist at:  
Data/songs.csv

### Menu System

**Playlist Menu**  
--- Playlist Menu ---

1. Add Song
2. Remove Song
3. Next Song
4. Previous Song
5. Shuffle
6. Stats
7. Visualisations
8. Import Songs from CSV
9. Exit

**Stats Menu**  
--- Stats Menu ---

1. Total Duration
2. Total Play Counts
3. Genre Counts
4. Exit

**Visualisations Menu**  
--- Visualisations ---

1. Songs per Duration
2. Songs per Genre
3. Most common title words
4. Exit

### Key Components

**SongNode (song_node.py)**  
Represents each song with:

- Title
- Artist
- Duration
- Genre

**Playlist (playlist.py)**  
Manages songs using a doubly linked list  
Handles navigation, shuffles, and imports

**Stats (stats.py)**  
Tracks:

- Total duration
- Play counts
- Genre distribution

**Graphs (graphs.py)**  
Generates visual insights using charts

### Limitations

Limitations include:

- Fixed CSV file path
- Data is lost upon refresh and must be re-imported from CSV File
- Users cannot search, sort, or filter songs within playlist
