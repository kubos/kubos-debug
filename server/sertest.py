#!/usr/bin/python3

from model import serialconn


try:
    ser = serialconn.open()
except:
    print ("No serial console")

if serialconn.login(ser, "kubos", "Kubos123"):
    req_dir = "/home/system/usr/local/bin"
    req_file = "/vagrant/Vagrantfile"
    serialconn.send_file(ser, req_file, req_dir)
