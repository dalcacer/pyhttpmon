#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__author__ = 'dalcacer'
__version__ = (0, 0, 1)

import requests
from pushbullet import PushBullet
import smtplib
import kaptan
import os
dirname, filename = os.path.split(os.path.abspath(__file__))
config = kaptan.Kaptan(handler="json")
config.import_config(dirname+"/config.json")


FAILRED = '\033[91m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'


def checkHTTP(dom):
    """
    Perform a simple HTTP-Get Request. If the outcome is 200 Ok, everything
    is fine.
    """
    try:
        r = requests.get(dom, verify=False, allow_redirects=False)
        if r.status_code is 200:
            #print("Host "+dom+OKGREEN+" ok."+ENDC)
            return True
    except:
        pass
    #print("Host "+dom+FAILRED+" appreantly down."+ENDC)
    return False


def notifyPushbullet(downlist):
    """
    """
    #prepare the interface
    pb = PushBullet(config.get("pushbullet_api_key"))
    devices = []

    #identify desired targets
    for device in pb.devices:
        devicename = device.name
        deviceno = device.device_id

        target = config.get("pushbullet_target_dev")
        if target is not "":
            if target == devicename:
                devices.append(deviceno)
        else:
            devices.append(deviceno)

    #prepare message
    message = "The host(s): \n"
    for dom in downlist:
        message += " "+dom+" \n"
    message += "seems to be down."

    #actually push the messages
    for deviceno in devices:
        device = pb.get(deviceno)
        push = device.push_note("server monitor", message)


def notifyEMail(downlist):
    """
    Use smtplib on a configured system to notify via email.
    """

    emailfrom = config.get("emailfrom")
    emailto = config.get("emailto")
    #prepare message
    message = "The host(s): \n"
    for dom in downlist:
        message += " "+dom+" \n"
    message += "seems to be down."

    template = "From: pyhttpmon <{FROMMAIL}>\n To: <{TO}> \nSubject: pyhttpmon\n\n{DOWNMESSAGE}"
    body = template.format(FROMMAIL=emailfrom, TO=emailto, DOWNMESSAGE=message)
    print("the body: "+body)
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(emailfrom, emailto, body)
    except Exception as e:
        print("failed to send mail "+e)
        pass

if __name__ == '__main__':
    downlist = []
    for dom in config.get("doms"):
        if checkHTTP(dom) is False:
            downlist.append(dom)
    if(len(downlist) > 0):
        if config.get("usepushbullet") is True:
            notifyPushbullet(downlist)
        if config.get("useemail") is True:
            notifyEMail(downlist)
