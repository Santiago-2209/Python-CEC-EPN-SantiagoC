# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:58:24 2020

@author: CEC
"""

import urllib.parse
import requests

main_api= "http://www.mapquestapi.com/directions/v2/route?"
orig="Washington"
dest="Baltimaore"
key="ExqZixXe4rARESciCgUEankNcAOj3vxr"
url= main_api+urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data=requests.get(url).json()
print(json_data)