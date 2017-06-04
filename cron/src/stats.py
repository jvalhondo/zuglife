import os
from slackclient import SlackClient
from blockchain import statistics

slack_token = os.environ['SLACK_TOKEN']
sc = SlackClient(slack_token)

def text_stats(stats):
    _text = '\n' + '*STATS*' + '\n' + '\n'

    attrs = ['trade_volume_btc', 'miners_revenue_usd', 'btc_mined', 'trade_volume_usd', 'difficulty',
             'minutes_between_blocks', 'number_of_transactions', 'hash_rate', 'timestamp', 'mined_blocks',
             'blocks_size', 'total_fees_btc', 'total_btc_sent', 'estimated_btc_sent', 'total_btc', 'total_blocks',
             'next_retarget', 'estimated_transaction_volume_usd', 'miners_revenue_btc', 'market_price_usd', ]

    for attr in attrs:
        _text += attr + ': ' + str(getattr(stats, attr)) + '\n'

    return _text

text = ''
# get stats
stats = statistics.get()
text += text_stats(stats)

sc.api_call("chat.postMessage", channel="#bots",text=text)
