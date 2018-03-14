import serial
import os
import sys
from time import sleep

SERIAL_DEV = "/dev/ttyUSB0"
SERIAL_SPEED = 115200

def send_read_line(ser, cmd):
    cmdstr = "%s\n" % cmd
    ser.write(cmdstr.encode())
    sleep(0.1)
    lines = ser.readlines()
    lines_str = ""
    for l in lines:
        lines_str += l.decode()
    return lines_str

def wait_on_string(ser, string):
    timeout = 10
    for i in range(1, timeout):
        lines = ser.readlines()
        for l in lines:
            if string in l.decode():
                return True
    return False

def send_file(ser, local_file, remote_folder):
    ser.write(("cd %s\n" % remote_folder).encode())
    #ser.write(("rz -w 8192\n").encode())
    #ser.close()
    os.system("stty -F %s %s" % (SERIAL_DEV, SERIAL_SPEED))
    os.system("sz -ybU -w 8192 %s > %s < %s" % (local_file, SERIAL_DEV, SERIAL_DEV))
    #os.system("sz %s" % local_file)

def login(ser, user, password):
    send_read_line(ser, "")
    if "#" in send_read_line(ser, ""):
        print("logged in")
        return True
    print ("logging in...")
    ser.write("\n".encode())
    if wait_on_string(ser, "login:"):
        ser.write(("%s\r\n" % user).encode())
        if wait_on_string(ser, "Password:"):
            ser.write(("%s\r\n" % password).encode())
            return wait_on_string(ser, "#")
    return False

def run_show_output(remote_file):
    global ser
    blank_lines = 0
    line = ""

    ser.write(("%s\n" % remote_file).encode())

    while blank_lines < 3:
        line = ser.readline().decode().strip()
        if line == "":
            blank_lines = blank_lines + 1
        else:
            blank_lines = 0
            print (line)

def open():
    ser = serial.Serial(SERIAL_DEV, SERIAL_SPEED, timeout=0.1)
    return ser

def close(ser):
    ser.close()
