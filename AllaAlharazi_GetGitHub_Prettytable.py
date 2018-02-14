#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:03:11 2018

@author: allo0o2a
"""

import json
import urllib.request as urllib2
from prettytable import PrettyTable


def get_info(user_id):
    api_url = 'https://api.github.com/users/' + user_id +'/repos'
    url_req = urllib2.Request(api_url, headers={ 'User-Agent': 'Safari/537.36', 'Content-Type': 'application/json'} , method='GET')
    try:
        response = urllib2.urlopen(url_req).read().decode('utf8')
    except: 
        return ('Invalid GitHub Username / or URL Access Forbidden')
    response_json = json.loads(response) 
    t1 = PrettyTable(['Name of the repository', 'Number of Commits'])
    for item in response_json:  
        try:
            api_url_2 = 'https://api.github.com/repos/' + user_id + '/' +item['name'] + '/commits'
            url_req_2 = urllib2.Request(api_url_2, headers={ 'User-Agent': 'Safari/537.36' , 'Content-Type': 'application/json'} , method='GET')
            response_2 = urllib2.urlopen(url_req_2).read().decode('utf8') 
            response_json_2 = json.loads(response_2)
            S = len(response_json_2)
        except:
            S = 0
        t1.add_row([item['name'],S])
    return (t1)

def main():
    user_id = input("Please enter your GitHub Username: ")
    print(get_info(user_id))
    
if __name__ == "__main__":
    main()
