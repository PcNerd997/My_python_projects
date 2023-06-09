import requests

spotify_api = "https://api.spotify.com/v1/search"
spotify_token_api_endpoint = "https://accounts.spotify.com/api/token"
spotify_token = "BQDV8SQz0j1gCzWjXSG_xBKh-g9j85fMcdXDb99hDZ-IqYkFLojgFZg4ZYTz0OIdKBQJ8ZONN1jcNBtji00Aq4F4qXitdKWn-axIioGLYEFPd6Uj8PFV"
my_id = "936d6cbd7b7944c794fb78c3be5ab75e"
my_screte = "ca82e5b767d7412d9b3e53ed9a72f99e"
token_endpoint_params = {
    "grant_type": "client_credentials",
    
}
header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# respons = requests.post(url = spotify_token_api_endpoint, headers= header,  params= token_endpoint_params)

# print(respons.text)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
auth_manag = SpotifyClientCredentials(client_id= my_id,
                                        client_secret= my_screte,)
sp = spotipy.Spotify(auth_manager= auth_manag)