from site_reader import Billboard
from spotify import SpotifyOps

# year = input("Which year do you want to travel to (YYYY-MM-DD) ?")
year=2025

bb = Billboard()
songs = bb.get_song_list()

sp = SpotifyOps()
song_uris = sp.get_songs(songs, year)
print(song_uris)


