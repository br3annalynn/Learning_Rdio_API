import rdio
import os
import json

CONSUMER_KEY = os.getenv('RDIO_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('RDIO_CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.getenv('MY_RDIO_ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('MY_RDIO_ACCESS_TOKEN_SECRET')

rdio_manager = rdio.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# Make an authorized call.
current_user = rdio_manager.current_user()
print current_user.key


# ##### Gets the users collection, including names and lengths
# user_collection = rdio_manager.get_albums_in_collection(user=current_user.key)

# print '**************number of albums: ', len(user_collection)

# for i in range(0, len(user_collection)):
#     tracks = rdio_manager.get_tracks_for_album_in_collection(user_collection[i].key, user=current_user.key)
#     print '******album %d: ' %(i + 1)
#     print 'number of tracks: ', len(tracks)
#     for track in tracks:
#         print 'song name: ', track.name, track.duration


##### Gets user's playlists
user_playlists = rdio_manager.get_playlists(extras=['tracks']).owned_playlists

for playlist in user_playlists:
    print 'Playlist Title: ', playlist.name
    playlist_tracks = playlist.tracks
    for track in playlist_tracks:
        print track.name, track.key








