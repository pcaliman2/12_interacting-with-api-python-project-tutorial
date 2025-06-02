import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#SodaEstereo: 2TieOXUFdPe8OrB8WYgKJy
artist_id = "2TieOXUFdPe8OrB8WYgKJy"

# Get the top tracks of an artist
results = spotify.artist_top_tracks(artist_id)

print(results)


