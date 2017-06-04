import os
from slackclient import SlackClient
from blockchain import exchangerates

slack_token = os.environ['SLACK_TOKEN']
sc = SlackClient(slack_token)

def text_ticker(ticker):
    _text = '*TICKER*' + '\n' + '\n'

    attrs = ['symbol', 'last', 'buy', 'sell', 'p15min', ]

    for attr in attrs:
        _text += attr + ': ' + str(getattr(ticker, attr)) + '\n'

    return _text

text = ''
# get ticker
ticker = exchangerates.get_ticker()
text += text_ticker(ticker['USD'])

sc.api_call("chat.postMessage", channel="#bots",text=text)
