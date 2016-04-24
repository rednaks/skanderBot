import requests
import json

API = 'https://api.api.ai/v1/'

AUTH = {'Authorization': ''}
master = None



def configure(key, a_master):
    AUTH['Authorization'] = 'Bearer ' + key
    
    global master
    master = a_master



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
            response = result['fulfillment']['speech']
            print('Response : '+result['fulfillment']['speech'])
            if result['action'] == 'input.unknown':
                response += 'I will ask my master @{} to teach me that :)'.format(master)

            return response
    else:
        print('AI::NOOK')
        print(r.text)



def greeting(sender):
    reply = 'Hello ' + sender
    return reply


ACTIONS = {'greeting': greeting}
