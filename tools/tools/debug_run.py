#!/usr/bin/env python

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run some remote commmand')
    parser.add_argument('command', help='command to run')
    parser.add_argument('-d', '--dir', help='directory to run command in')

    args = parser.parse_args()

    data = { 'command' : args.command }

    if args.dir != None:
        data['dir'] = args.dir

    r = requests.post('http://192.168.1.205:8000/run', json=data)

    print r.text

if __name__ == '__main__':
    main()
