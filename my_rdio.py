
import rdio
import os

CONSUMER_KEY = os.getenv('RDIO_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('RDIO_CONSUMER_SECRET')

rdio_manager = rdio.Api(CONSUMER_KEY, CONSUMER_SECRET)
user = rdio_manager.find_user('breannalynn@gmail.com')
print '%s %s\'s key is: %s.' % (user.first_name, user.last_name, user.key)

# Set authorization: get authorization URL, then pass back the PIN.
token_dict = rdio_manager.get_token_and_login_url()
print 'Authorize this application at: %s?oauth_token=%s' % (
    token_dict['login_url'], token_dict['oauth_token'])

print 'oauth_token: ', token_dict['oauth_token']
print 'oauth_token_secret: ', token_dict['oauth_token_secret']

token_secret = token_dict['oauth_token_secret']
oauth_verifier = raw_input('Enter the PIN / oAuth verifier: ').strip()
token = raw_input('Enter oauth_token parameter from URL: ').strip()
request_token = {"oauth_token":token, "oauth_token_secret":token_secret}
authorization_dict = rdio_manager.authorize_with_verifier(oauth_verifier, request_token)

# Get back key and secret. rdio_manager is now authorized
# on the user's behalf.
print 'Access token key: %s' % authorization_dict['oauth_token']
print 'Access token secret: %s' % authorization_dict['oauth_token_secret']

# Make an authorized call.
current_user = rdio_manager.current_user()
print 'The full name of the current user is %s.' % (
    current_user.name,)


# user_collection = rdio_manager.get_albums_in_collection(user=user.key)
# print user_collection
#     name='Whoopie!',
#     description='A test playlist for the Rdio API.',
#     tracks=album.track_keys,
#     extras=['trackKeys',])
# # Have some fun.
# search_object = rdio_manager.search(
#         query='Big Echo',
#         types=['Albums',],
#         extras=['trackKeys',])
# album = search_object.results[0]
# print "Found album %s by %s." % (album.name, album.artist_name,)
# new_playlist = rdio_manager.create_playlist(
#     name='Whoopie!',
#     description='A test playlist for the Rdio API.',
#     tracks=album.track_keys,
#     extras=['trackKeys',])
# print "Just made playlist %s with %i tracks at %s! Has tracks: " % (
#         new_playlist.name,
#         new_playlist.track_count,
#         new_playlist.short_url)
# tracks = rdio_manager.get(new_playlist.track_keys)
# for t in tracks: print "%s (Duration: %i seconds)" % (t.name, t.duration.seconds,)





