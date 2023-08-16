import requests

CLIENT_ID = "700af02d5bf54252ba4cf056cabf70b6"
CLIENT_SECRET = "c1a65c4c6f8e40dfbbdc7decbd57ecf7"

def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data, auth=(client_id, client_secret))
    access_token = response.json().get("access_token")
    return access_token

def get_recommendations_by_genres(access_token, genres):
    url = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "seed_genres": ",".join(genres),
        "limit": 10  # Number of recommendations
    }
    response = requests.get(url, headers=headers, params=params)
    recommendations = response.json().get("tracks", [])
    return recommendations

def get_recommendations_by_artists(access_token, artists):
    url = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "seed_artists": ",".join(artists),
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)
    recommendations = response.json().get("tracks", [])
    return recommendations


# Example usage
if __name__ == "__main__":
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    favorite_genres = ["sad", "indian"]
    genre_recommendations = get_recommendations_by_genres(access_token, favorite_genres)
    print("Recommendations based on genres:")
    for i, track in enumerate(genre_recommendations, start=1):
        print(f"{i}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

    favorite_artists = ["0Y5tJX1MQlPlqiwlOH1tJY", "6KImCVD70vtIoJWnq6nGn3"]  # Example artist IDs
    artist_recommendations = get_recommendations_by_artists(access_token, favorite_artists)
    print("\nRecommendations based on artists:")
    for i, track in enumerate(artist_recommendations, start=1):
        print(f"{i}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
