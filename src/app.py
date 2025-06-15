import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#==============================================================================
#Paso 1: Crear una cuenta de desarrollador de Spotify
#Paso 2: Configuración inicial
#==============================================================================
# Cargar variables del archivo .env
load_dotenv()

#==============================================================================
#Paso 3 del Proyecto
#==============================================================================
# # Obtener credenciales
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#==============================================================================
#Paso 4: Inicializar la biblioteca Spotipy
##==============================================================================
# # Autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#==============================================================================
#Paso 5: Realizar solicitudes a la API
##==============================================================================
# ID del artista
artist_id = "7An4yvF7hDYDolN4m5zKBp"
#Soda Stereo

# Get the top tracks of an artist
results = spotify.artist_top_tracks(artist_id)
# Obtener top tracks
#results = spotify.artist_top_tracks(artist_id)

#Una vez tengas la respuesta de la API, quédate con el elemento tracks, 
#que contendrá las canciones con más reproducciones del artista, 
#quédate con el nombre de la canción, la popularidad y la duración (en minutos).
CancionesT10 = []
for track in results['tracks']:
    CancionesT10.append({'Cancion': track['name'],
            'CancionesFrame': track['popularity'],
            'Duracion': track['duration_ms'] / 60000 #Esta en Mill Segundos y la quieren en Minutos
    })                       
                    
print(CancionesT10)

#==============================================================================
#Paso 6: Transformar a Pandas DataFrame
##==============================================================================
CancionesFrame = pd.DataFrame(CancionesT10)

for i in CancionesFrame['Cancion']:
    print(i)

print(CancionesFrame)

#===============================================================================
#Paso 6: Transformar a Pandas DataFrame
##==============================================================================
plt.scatter(CancionesFrame['Duracion'], CancionesFrame['CancionesFrame'])
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.title('Relationship between duration and popularity')
plt.show()




