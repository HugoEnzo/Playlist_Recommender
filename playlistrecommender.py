import spotipy
import json
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

cid = '3032d83d437a43cdac6901199cb01c7f'
csecret = '4ea77e0b628f462fa6d9b29e3fd6d75f'
spotify_uri = '0z8wl8E5xW6Pg0tiNKVQbf'

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret =csecret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager) #makes spotipy object

#playlist_obj = json.loads(playlist_json, indent =2)

#print(playlist_json['items']. ['track'])

#playlist_json['items'['track']]
playlist_dict = sp.playlist_tracks(spotify_uri)

playlist_track_info_list=[]
genre_list_playlist=[]



for track in playlist_dict['items']:
    track_uri = track['track']['uri']

    
    track_name = track['track']['name']

    artist_uri = track['track']['artists'][0]['uri']
    artist_info = sp.artist(artist_uri)
 
    artist_name = artist_info['name']
    artist_genre = artist_info['genres']
    artist_popularity = artist_info['popularity']

    album_name = track['track']['album']['name']
    track_popularity = track['track']['popularity']
    
    genre_list =[artist_genre]
    genre_list_playlist.append(genre_list)

    carry_over_list = [track_name, track_uri, track_popularity, artist_uri, artist_name, artist_genre, artist_popularity, album_name]
    playlist_track_info_list.append(carry_over_list) 

'''
Indexes for Values :

track_name = 0
track_uri = 1
track_popularity = 2
artist_uri = 3
artist_name = 4
artist_genre = 5
artist_popularity = 6
album_name = 7

'''
#playlist_track_info_list.write('metadata.txt','w')

pprint.pprint(genre_list_playlist, indent =2)

