# Script to send messages to FB Messenger via FB Messenger Send API
import requests

FB_ACCESS_TOKEN = 'EAAVVA1mZAbx4BAOMqkvQZCEZBbpTi7CMXE78V37cAcfV8KQgaoWv6cH3OHsqDBpvUEtgls4cmQNqBZBqZBZBdLNEZA08jYABi641Bjxt5PnAL2JzjbedCNs9Fk5IAZBxyjl0QRNjAV9yYIWLgvZACcrnEnIZCV7jPmBzrFMhAQB2VEZAgZDZD'
SEND_API_URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + 'EAAVVA1mZAbx4BAOMqkvQZCEZBbpTi7CMXE78V37cAcfV8KQgaoWv6cH3OHsqDBpvUEtgls4cmQNqBZBqZBZBdLNEZA08jYABi641Bjxt5PnAL2JzjbedCNs9Fk5IAZBxyjl0QRNjAV9yYIWLgvZACcrnEnIZCV7jPmBzrFMhAQB2VEZAgZDZD'
    
def send_genres_message(messenger_id, text, genre):
    # Package params into dictionaries for POST request
    quick_replies = [] # append to
    for g in genre:
        # https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies
        '''
        {
            "content_type":"text",
            "title":"CATEGORY NAME",
            "payload":"CATEGORY NAME"
        }
        '''
        quick_replies.append({"content_type":"text", "title":g,"payload":g})

    recipient = {'id':messenger_id}
    message = {
        'text':text,
        'quick_replies':quick_replies
    }
    params = {
        'recipient':recipient,
        'message':message
    }

    # Send POST request to Facebook Messenger Send API to send coordinates message
    r = requests.post(SEND_API_URL, json=params)
