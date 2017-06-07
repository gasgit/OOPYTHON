#!/usr/bin/python

'''

    import urlib2, json modules 

'''


import urllib2

import json



URL_GIT_USER_INFO = "https://api.github.com/users/gasgit"
'''
    get user info
'''
URL_REPO_INFO = "https://api.github.com/repos/gasgit/Ruby"

'''
    get repo info
'''




def user_data(url):
    '''
        pass url str, parse response to json, print
    '''
    res = urllib2.urlopen(url)

    json_values = json.load(res)

    p_json = json.dumps(json_values, sort_keys=True, indent=4)

    print p_json
    print '************************** end *****************************'

user_data(URL_GIT_USER_INFO)
user_data(URL_REPO_INFO)







