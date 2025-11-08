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
        scope = "playlist-modify-public"
        self.uri_list = []

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=scope
        ))

        user = self.sp.current_user()
        print("Authentication successful!")
        print(f"Logged in as: {user['display_name']} ({user['id']})")
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
        return self.uri_list

        # # test
        # query = f"track:{songs} year:{year}"
        # result = self.sp.search(q=query, type='track', limit=1)
        # print(result)

# testing
# t1 = SpotifyOps()
# t1.get_songs("Evil Jordan",2025)




