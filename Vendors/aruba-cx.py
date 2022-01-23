#!/usr/bin/env python3

# Import modules
import requests
import urllib3, urllib
import io
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ArubaCX:
    """
    login(ip_address) funcation to login to the RestAPI os a switch

    logout(ip_address) function to logout of the RestAPI of a switch
    """

    # def login(ip_address):
    # def logout(ip_address):
    # def arp()