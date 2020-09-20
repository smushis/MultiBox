
import spotipy.util as util
import json

# generates spotify token using credentials from token_file
# if the token is expired, a web page opens up to acquire a new token
def generate_token(scope, token_file, refresh=False):
    with open(token_file, "r") as file:
        auth = json.load(file)
	# update with new token value
    try:
        token = util.prompt_for_user_token(auth["username"], scope, client_id=auth["CLIENT_ID"], client_secret=auth["CLIENT_SECRET"], redirect_uri=auth["REDIRECT_URI"])
    except:
        token = None
        
    if token != None:
        print("New token generated")
        auth["token"] = token
        
    with open(token_file, "w") as file:
        json.dump(auth, file)

if __name__ == "__main__":
	generate_token("user-read-currently-playing user-library-modify", "spotify_token.oauth")
