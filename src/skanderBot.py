import requests
import json
import os
import time

import ai
import tg
from tg import getUpdates, sendMessage


root = os.path.dirname(__file__)
config_path = 'bot.conf'

def load_config():
    config = None

    print(os.path.join(root, config_path))
    with open(os.path.join(root, config_path), 'r') as f:
        config = json.load(f)

    return config

def updates_loop():
    update_id = None
    while True:
        try:
            updates = getUpdates(update_id)

            if len(updates['result']) == 0:
                # no results,
                # let's take some rest...
                time.sleep(0.5)

            for u in updates['result']:
                update_id = u['update_id']
                user = u['message']['from']['username']
                msg = '{}: {}'.format(user, u['message']['text'].encode('utf8'))
                tg.Logger.info(msg)
                resp = ai.ask(user, msg)
                try:
                    sendMessage(u['message']['chat']['id'], resp, u['message']['message_id'])
                except Exception as e:
                    tg.Logger.err('Something wrong happend with the networking '
                            + 'while replying ... we will retry later.')
                    updates['result'].append(u)
        except Exception as e:
            tg.Logger.err("Networking error ...")


if __name__ == '__main__':

    config = load_config()
    ai.configure(config['ai_key'], config['master'])
    tg.configure(config['tg_key'])

    updates_loop()



