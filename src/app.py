import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Cargar variables del archivo .env
load_dotenv()

# Obtener credenciales
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# ID del artista
artist_id = "7An4yvF7hDYDolN4m5zKBp"

# Get the top tracks of an artist
results = spotify.artist_top_tracks(artist_id)
# Obtener top tracks
#results = spotify.artist_top_tracks(artist_id)

CancionesT10 = []
for track in results['tracks']:
    CancionesT10.append({'Canciom': track['name']})

CancionesFrame = pd.DataFrame(CancionesT10)
for i in CancionesFrame['Canciom']:
    print(i)