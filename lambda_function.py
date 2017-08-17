# coding:utf-8


import requests
import json
import os
import logging
import traceback


slack_url = os.environ['SLACK_URL']
log_level = os.environ.get('LOG_LEVEL', 'INFO')
channel = os.environ.get('CHANNEL', '#general')

logger = logging.getLogger()

if log_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

def send_message(content, channel):
    payload_dic = {
        "text": content,
        "channel": channel,
    }
    logger.debug(payload_dic)
    response = requests.post(slack_url, data=json.dumps(payload_dic))
    logger.debug(response.text)


def lambda_handler(event, context):

    try:
        logger.debug(event)
        icon = event.get('icon',':question:')
        logger.debug(icon)

        send_message(
            u':hourglass_flowing_sand:{icon}:申込がありました'.format(
                icon=icon
            ),
            channel
        )
        return event

    except Exception as e:
        send_message(traceback.format_exc(), '#general')
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())
