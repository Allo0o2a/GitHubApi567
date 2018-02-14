#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:03:11 2018

@author: allo0o2a
"""

import json
import requests


def get_info(user_id):
    api_url1 = requests.get('https://api.github.com/users/' + user_id + '/repos')
    response_json1 = json.loads(api_url1.text)
    
    try:
        response_json1[0]['name']
    except: 
        return ('Invalid GitHub Username')
    
    li = []
    for item in response_json1:  
        api_url_2 = requests.get('https://api.github.com/repos/' + user_id + '/' + item['name'] + '/commits')
        response_json2 = json.loads(api_url_2.text)
        if 'name' in api_url_2.text:
            a = (len(response_json2))
        else:
            a= 0
        li.append((item['name'],a))
    return li

def main():
    user_id = input("Please enter your GitHub Username: ")
    print(get_info(user_id))

      
if __name__ == "__main__":
    main()
