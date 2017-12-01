# Script to send API requests to SoundCloud API
import soundcloud

def songs(source):
    
    client = soundcloud.Client(client_id='Bo3dsyRIYdM3bp3SnNQ9xl3ax0IyWu38')

    # find all tracks with the genre chosen by user
    try:
        tracks = client.get('/tracks', genres=source)
    except Exception, e:
        print 'Error: %s, Status Code: %d' % (e.message, e.response.status_code)

    text = tracks.json()['songs']
    return text