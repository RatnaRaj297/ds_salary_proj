# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:27:04 2020

@author: Ratnaraj
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {'input' : data_in}

r = requests.get(URL, headers = headers, json = data)

print(r.json())