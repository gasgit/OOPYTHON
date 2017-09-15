#!/usr/bin/python

import json

from pprint import pprint

''' read geojson file, parse a nd print'''
try:
    with open('Scenic_Views.geojson') as data_file:

        data = json.load(data_file)
        # check data type ' dict '
        print type(data)
        
        # print all
        #data['features'][0]['geometry']
        #j_data = json.dumps(data)
        #pprint(data)

        #iterarte over data dict and unpack 
        for feature in data['features']:
            print feature['geometry']['type']
            print feature['geometry']['coordinates']
            print feature['properties']['CreationDate']

            if feature['properties']['Name'] == 'V24':
                
                print feature['properties']['Angle']
            


except IOError as e:
    print e