import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth
import privVars


# Setting spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=privVars.client_id,
                                               client_secret=privVars.client_secret,
                                               redirect_uri="http://localhost:1234",
                                               scope="user-library-read,playlist-modify-private,playlist-modify-public")) 

recently_liked_ids = []

results = sp.current_user_saved_tracks(limit=20) # Change limit=20 to the amount of tracks you want in your playlist
for idx, item in enumerate(results['items']):
    track = item['track']
    #print(idx, track['artists'][0]['name'], " – ", track['name'], track['id']) #For debugging
    recently_liked_ids.append(track["id"])

#random.shuffle(recently_liked_ids) #Add this line to shuffle your playlist


sp.playlist_replace_items(privVars.playlistID, recently_liked_ids)