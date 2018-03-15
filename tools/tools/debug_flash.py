#!/usr/bin/env python

import requests
import argparse
import json
import os
import config

FLASH_URL = "%s/flash" % config.URL

def main():
    parser = argparse.ArgumentParser(description='Sends file to remote device')
    parser.add_argument('file', help='file to send')
    parser.add_argument('-d', '--dir', help='directory to place file in')

    args = parser.parse_args()

    files = {}
    data = {}

    try:
        files['file'] = (os.path.basename(args.file), open(args.file, 'rb'), 'application/octet-stream')
    except:
        print "No file found"
        return

    if args.dir != None:
        data['dir'] = args.dir
        files['json'] = ('json', json.dumps(data), 'application/json')

    try:
        r = requests.post(FLASH_URL, files = files)
    except:
        print "Could not connect to server"
        return

    print r.text

if __name__ == '__main__':
    main()
