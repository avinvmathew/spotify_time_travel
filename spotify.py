import os
from dotenv import load_dotenv
import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY100_Client_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY100_Client_Secret')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

class SpotifyOps:
    def __init__(self):
        self.playlist_link = None
        self.playlist_id = None
        scope = "playlist-modify-public playlist-modify-private"
        self.uri_list = []

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=scope
        ))

        self.user = self.sp.current_user()
        print("Authentication successful!")
        print(f"Logged in as: {self.user['display_name']} ({self.user['id']})")
    def get_songs(self, songs, year):
        for track in songs:
            query = f"track:{track} year:{year}"
            try:
                result = self.sp.search(q=query, type='track', limit=1)
                items = result['tracks']['items']
                if not items:
                    print(f"Track : {track} not found!")
                    continue
                track_uri = items[0]['uri']
                self.uri_list.append(track_uri)
            except SpotifyException as e :
                print(f"Spotify API error for track : {track}")
            except (KeyError, IndexError):
                print(f"Unexpected response structure for track: {track}")
            except Exception as e:
                print(f"The track : {track} is not availiable!")

        self.create_time_playlist(year)
        # return self.uri_list

    def create_time_playlist(self,year):

        playlist_name = f"Billboard Hot 100 of {year} (Python project)"
        desc = "This playlist was created using a python script in python using spotipy as a part of udemy python bootcamp by Dr. Angela Yu"
        playlist = self.sp.user_playlist_create(user=self.user['id'], name=playlist_name, public=False, collaborative=False,description=desc)
        self.playlist_id = playlist['id']
        self.playlist_link = playlist['external_urls']['spotify']
        self.add_songs_to_playlist()

    def add_songs_to_playlist(self):
        self.sp.playlist_add_items(playlist_id=self.playlist_id, items=self.uri_list)
        print(f"Playlist successfully created! at {self.playlist_link}")



# testing
# t1 = SpotifyOps()
# t1.get_songs("Evil Jordan",2025)




