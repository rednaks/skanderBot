import requests
import json

API = 'https://api.telegram.org/bot'


class Logger:
    def __init__(self):
        pass

    def err(message):
        print('TG::ERR:: {}'.format(message))

    def info(message):
        print('TG::INFO:: {}'.format(message))


def configure(a_key):
    global API
    API += a_key

def sendMessage(user, text):
    url = API + '/sendMessage?chat_id={}&text={}'.format(user, text)

    res = requests.get(url)

    if res.ok:
        Logger.info('Message sent')
    else:
        Logger.err("Couldn't send the message")


def getUpdates(last_update_id):
    url = API + '/getUpdates'

    if last_update_id is not None:
        url += '?offset={}'.format(last_update_id + 1)

    res = requests.get(url)

    if res.ok:
        response = res.json()
        Logger.info('We recieved: {}'.format(response))
        return response
    else:
        Logger.err("Something wrong happend while sending")


