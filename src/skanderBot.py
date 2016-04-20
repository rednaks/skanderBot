import requests
import json

import ai

API = 'https://api.telegram.org/bot'

def load_config():
    f = open('bot.conf', 'r')
    config = json.load(f)
    f.close()
    return config

def sendMessage(user, text):
    url = API + '/sendMessage?chat_id={}&text={}'.format(user, text)

    req = requests.get(url)

    if req.ok :
        print 'bot::messagesent'
        response = req.json()
    else:
        print req.text
        print 'bot::messageerror'

def getUpdates(last_update_id):
    
    url = API + '/getUpdates'

    if last_update_id is not None:
        url = url + '?offset={}'.format(last_update_id +1)

    req = requests.get(url)
    if(req.ok):
        return req.json()
    else:
        print 'NOT OK'

def updates_loop():
    update_id = None
    while True:
        updates = getUpdates(update_id)

        for u in updates['result']:
            update_id = u['update_id']
            user = u['message']['from']['username']
            msg = '{}: {}'.format(user, u['message']['text'].encode('utf8'))
            print msg
            resp = ai.ask(user, msg)
            sendMessage(u['message']['chat']['id'], resp)


if __name__ == '__main__':

    config = load_config()
    ai.configure(config['ai_key'])

    API = API + config['tg_key']

    updates_loop()



