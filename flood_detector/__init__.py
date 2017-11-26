from . import _PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import os
import logging
import logging.handlers
from twilio.rest import Client

account = os.environ['TWILIO_ACCOUNT']
token = os.environ['TWILIO_TOKEN']
number = os.environ['TWILIO_NUMBER']
contacts = os.environ['FLOOD_CONTACTS'].split(',')


STARTUP_MSG = "This is Dan & Kelly's flood monitoring system. I'm awake."
ALERT_MSG = ("This is Dan & Kelly's flood monitoring system. "
             "I'm getting wet! Check the basement!")


logger = logging.getLogger('flood_monitoring')
logger.setLevel(logging.INFO)
ch = logging.handlers.RotatingFileHandler('/var/log/flood_monitor/flood_monitor.log',
                                          maxBytes=10000000, backupCount=9)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)
    client = Client(account, token)
    for contact in contacts:
        message = client.messages.create(to=contact, from_=number,
                                         body=STARTUP_MSG)
	logger.info('SMS %r', message)


def handle_change(x):
    if x == 1:
        logger.warn('Stopped raining')
        pass
    if x == 0:
        logger.warn('Started raining')
        client = Client(account, token)
        for contact in  contacts:
            message = client.messages.create(to=contact, from_=number,
                                             body=ALERT_MSG)
	    logger.info('SMS %r', message)

def loop():
    status = 1
    while True:
        logger.info('%s', ADC.read(0))
        
        tmp = GPIO.input(DO);
        if tmp != status:
            handle_change(tmp)
            status = tmp
        
        time.sleep(0.2)
