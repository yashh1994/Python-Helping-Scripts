import requests
import base64

# Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Encode client ID and secret
encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

# Get access token
auth_url = "https://accounts.spotify.com/api/token"
auth_response = requests.post(auth_url, headers={
    "Authorization": f"Basic BQAIJz8WmGyq2MoyccIbnQohQvBScbdVja35WrHndSRJ1RjMCRy40LIb4KBRW1itZ7E"
}, data={
    "grant_type": "client_credentials"
})

access_token = auth_response.json().get("access_token")

# Get recommendations based on seed genres
recommendations_url = "https://api.spotify.com/v1/recommendations"
params = {
    "seed_genres": "pop,rock",
    "limit": 10
}

recommendations_response = requests.get(recommendations_url, headers={
    "Authorization": f"Bearer {access_token}"
}, params=params)

tracks = recommendations_response.json().get("tracks", [])

for track in tracks:
    print(f"Track: {track['name']}, Artist: {track['artists'][0]['name']}, Genres: {track['album']['genres']}")
