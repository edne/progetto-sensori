import logging
import configparser

import smtplib
from email.message import EmailMessage


config = configparser.ConfigParser()
config.read('config.ini')

debug = config['GENERAL'].getboolean('debug')
api_key = config['GENERAL']['api_key']
from_mail = config['GENERAL']['from_mail']
dest_mail = config['GENERAL']['dest_mail']


# Per stampare informazioni
if debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(logging.INFO)

logger = logging.getLogger(__name__)


def send_message(msg):
    logger.debug('Creating server')
    server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)

    server.set_debuglevel(debug)

    logger.debug('Login')
    server.login('apikey', api_key)

    logger.debug('Sending')
    server.send_message(msg)

    logger.debug('Done')
    server.quit()


def new_message():
    msg = EmailMessage()
    msg.set_content('Test mail')

    msg['Subject'] = 'Test Sensore'
    msg['From'] = from_mail
    msg['To'] = dest_mail

    return msg


if __name__ == '__main__':
    msg = new_message()
    send_message(msg)
