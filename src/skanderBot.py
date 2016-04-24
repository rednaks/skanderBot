import requests
import json

import ai
import tg
from tg import getUpdates, sendMessage

def load_config():
    config = None
    with open('bot.conf', 'r') as f:
        config = json.load(f)

    return config

def updates_loop():
    update_id = None
    while True:
        updates = getUpdates(update_id)

        for u in updates['result']:
            update_id = u['update_id']
            user = u['message']['from']['username']
            msg = '{}: {}'.format(user, u['message']['text'].encode('utf8'))
            tg.Logger.info(msg)
            resp = ai.ask(user, msg)
            sendMessage(u['message']['chat']['id'], resp)


if __name__ == '__main__':

    config = load_config()
    ai.configure(config['ai_key'])
    tg.configure(config['tg_key'])

    updates_loop()



