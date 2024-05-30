import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyPlayer:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.sp_oauth = SpotifyOAuth(
            client_id = client_id,
            client_secret = client_secret,
            redirect_uri = redirect_uri,
            scope = scope
        )
        self.token_info = self.sp_oauth.get_cached_token()
        if not self.token_info:
            auth_url = self.sp_oauth.get_authorize_url()
            print(f"Please navigate here: {auth_url}")
            response = input("Paste the URL you were redirected to: ")
            code = self.sp_oauth.parse_response_code(response)
            self.token_info = self.sp_oauth.get_access_token(code)

        self.sp = spotipy.Spotify(auth=self.token_info['access_token'])



