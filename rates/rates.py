#!/usr/bin/python

"""
    get currency conversion rates with euro as base
    using fixer.io api
"""

import urllib2

import json


def rates():
    """
        function to get rates
    """
    currency_url = "http://api.fixer.io/latest"

    try:
        res = urllib2.urlopen(currency_url)

    except urllib2.HTTPError as e:
        print e.code
        print e.read()

    json_values = json.load(res)

    p_json = json.dumps(json_values, sort_keys=True, indent=4)

    print p_json

    json_results = {}
    for key, value in json_values.items():
        if key == "rates":
            json_results.update(value)

    print json_results

    for key, value in json_results.items():
        print key, value
    return json_results

rates()
