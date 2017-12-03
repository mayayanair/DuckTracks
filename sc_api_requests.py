# Script to send API requests to SoundCloud API
import soundcloud

def songs(source):
    
    client = soundcloud.Client(client_id='Bo3dsyRIYdM3bp3SnNQ9xl3ax0IyWu38')

    # find all tracks with the genre chosen by user
    tracks = client.get('/tracks', genres=source)

    return tracks
