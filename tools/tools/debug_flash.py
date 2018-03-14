#!/usr/bin/env python

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Sends file to remote device')
    parser.add_argument('file', help='file to send')
    parser.add_argument('-d', '--dir', help='directory to place file in')

    args = parser.parse_args()

    try:
        files = { 'file' : open(args.file, 'rb') }
    except:
        print "No file found"
        return

    data = { }

    if args.dir != None:
        data['dir'] = args.dir

    print files

    r = requests.post('http://192.168.1.205:8000/flash', files=files, json=data)

    print r.text

if __name__ == '__main__':
    main()
