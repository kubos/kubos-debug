import serial
import os
import sys
from time import sleep
import subprocess

SERIAL_DEV = "/dev/ttyIOBC"
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
    os.system("stty -F %s %s" % (SERIAL_DEV, SERIAL_SPEED))
    #os.system("sz -ybU -w 8192 %s > %s < %s" % (local_file, SERIAL_DEV, SERIAL_DEV))
    #output = subprocess.call("sz -ybU -w 8192 %s > %s < %s" % (local_file, SERIAL_DEV, SERIAL_DEV), shell=True)
    #print(output)


    cmd = ["sz", "-ybU", "-w", "8192", local_file, ">", SERIAL_DEV, "<", SERIAL_DEV]
    print(cmd)
    p = subprocess.Popen("sz -ybU -w 8192 %s > %s < %s" % (local_file, SERIAL_DEV, SERIAL_DEV), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p
    # while True:
    #     output = p.stderr.readline()
    #     if output == '' and p.poll() is not None:
    #         break
    #     if output:
    #         print("output")
    #         print(output.strip())
    #print(p.communicate())
    # output = subprocess.check_output(cmd)
    # print(output)

    # process = subprocess.Popen(
    #     #"sz -ybU -w 8192 %s > %s < %s" % (local_file, SERIAL_DEV, SERIAL_DEV),
    #     cmd,
    #     stdout=subprocess.PIPE
    # )
    # while True:
    #     output = process.stdout.readline()
    #     if output == '' and process.poll() is not None:
    #         break
    #     if output:
    #         print(output.strip())

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
