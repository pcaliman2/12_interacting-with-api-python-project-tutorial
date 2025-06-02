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
artist_id = "2TieOXUFdPe8OrB8WYgKJy"

# Obtener top tracks
results = spotify.artist_top_tracks(artist_id)

# Mostrar resultados
#print(results)
print(client_id)
print(client_secret)
