# SpotifyRecentlyLiked

A spotify app to add your recently liked tracks to a playlist.

## Get started

### Install dependencies

Run `pip install -r requirements.txt` in the repo.

### Setting up
First, create a file called `privVars.py` in the root of the repo and add the following to this file: 
```
client_id = ""

client_secret= ""

playlistID = ""
```
Then go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). Create a new app and enter `http://localhost:1234` in the redirect URIs field.
Once your app is created go to Settings, copy the Client ID and paste it in the `client_id` field of the privVars file then click on View client secret, copy it and paste it in the `client_secret` field.

Once this is done create a new playlist on your spotify account and copy your playlist ID (if you do not know how to do it put your playlist URL on this website https://spotifyplaylistarchive.com/get-playlist-id) and paste it on the playlistID field of the privVars file.

Then launch the program once and your web browser should ask you to login to your spotify account.

Feel free to open an issue if you have any problem!
