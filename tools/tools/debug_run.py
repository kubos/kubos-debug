#!/usr/bin/env python

import requests
import argparse
import config

RUN_URL = "%s/run" % config.URL

def main():
    parser = argparse.ArgumentParser(description='Run some remote commmand')
    parser.add_argument('command', help='command to run')
    parser.add_argument('-d', '--dir', help='directory to run command in')

    args = parser.parse_args()

    data = { 'command' : args.command }

    if args.dir != None:
        data['dir'] = args.dir

    try:
        r = requests.post(RUN_URL, json=data)
    except:
        print "Could not connect to server"
        return

    print r.text

if __name__ == '__main__':
    main()
