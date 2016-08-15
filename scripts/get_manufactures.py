#!/usr/bin/python
# -*- coding: latin1 -*-

import sys, pprint

if(len(sys.argv) < 2):
    print 'need file manufactures.txt'
    exit()
# open file and read file
filebrands = sys.argv[1]



def init():
    output = '['
    with open(filebrands, "r") as ins:
        n = 0
        for line in ins:
            line = line.strip()
            print line
            n += 1
            output+='{ "model": "inventory.manufacture", "pk": '+str(n)+', "fields": { "name": "'+(line)+'", "created": "2016-08-15 18:15:49.147097", "modified": "2016-08-15 18:15:49.147097"} },'

    # write final file
    output = output[:-1]+']'
    f = open('manufactures.json','wb')
    f.write(output) # write header content
    f.close

init()
