#!/usr/bin/env python

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Sends file to remote device')
    parser.add_argument('file', help='file to send')
    parser.add_argument('-d', '--dir', help='directory to place file in')

    args = parser.parse_args()

    data = { 'file' : args.file }

    if args.dir != None:
        data['dir'] = args.dir

    r = requests.post('http://192.168.1.205:8000/flash', data)

    print r.text
