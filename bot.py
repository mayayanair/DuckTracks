# Script that houses main logic of bot
from messenger_parser import MessengerParser
from sc_api_requests import songs
from messenger_api_requests import send_genres_message
from helpers import response
from db import User
from send import GenericTemplateMessage, GenericTemplateElement, URLButton 

genres = ['Classical','Country','Dance & EDM','Folk & Singer-Songwriter','Hip-hop & Rap','Indie','Latin','Pop','R&B & Soul','Trap','World']

def response_handler(request):
     # Parse request and get the data we want out of it like messenger_id, text, and coordinates.
    messenger_parser = MessengerParser(request)

    # Get user object from database so we can see the state of our user.
    try:
        user = User.select().where(User.messenger_id == messenger_parser.messenger_id).get()
    except:
        # If user doesn't exist, we create them. This would be a first time user.
        user = User.create(messenger_id=messenger_parser.messenger_id, state='ask_type')
        
    # Here we need to decide what we need to do next for our user
    if user.state == 'ask_type':
        # ask user what genre
        type_handler(messenger_parser, user)
    else:
        # call api and get results
        results_handler(messenger_parser, user)

    # return the response to Facebook.
    return response()

def type_handler(messenger_parser, user):
    genres_text = 'Please choose from the following genres: '
    send_genres_message(user.messenger_id, genres_text, genres)
    user.state = 'ask_results'
    user.save()


def results_handler(messenger_parser, user):

    text = messenger_parser.text
    if text not in set(genres):
        type_handler(messenger_parser, user)
        return
    
    result = songs(text)
    elements = []
    count = 0 
    for a in result:
        if count > 10:
            break
        title = a.title
        item_url = a.permalink_url
        image_url = a.artwork_url

        b = URLButton('Listen to Song', item_url)
        elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 
        count += 1

    mess = GenericTemplateMessage(elements, user.messenger_id)
    mess.send()
    user.state = 'ask_type'
    user.save()
