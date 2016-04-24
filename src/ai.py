import requests
import json

API = 'https://api.api.ai/v1/'

AUTH = {'Authorization': ''}



def configure(key):
    AUTH['Authorization'] = 'Bearer ' + key



def ask(sender, msg):

    url = API + 'query?v=20150910&lang=en&query='+ msg

    print(url)
    r = requests.get(url, headers=AUTH)

    if r.ok :
        print("AI::OK")
        result =  r.json()['result']


        msg = "Sorry I don't understand yet what you're saying, pealse ask my master @rednaks to implement it."
        try: 
            print(result)
            print(result['action'])
            msg =  ACTIONS[result['action']](sender)
            return msg
        except KeyError:
            # the action was not implemented, let's see
            # what the api.ai propose
            print('Response : '+result['fulfillment']['speech'])
            return (result['fulfillment'])['speech']
    else:
        print('AI::NOOK')
        print(r.text)



def greeting(sender):
    reply = 'Hello ' + sender
    return reply


ACTIONS = {'greeting': greeting}
