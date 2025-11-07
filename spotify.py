import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY100_Client_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY100_Client_Secret')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

user = sp.current_user()
print("Authentication successful!")
print(f"Logged in as: {user['display_name']} ({user['id']})")




