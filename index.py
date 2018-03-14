from flask import Flask, request
from model import serialconn
import click
import os, pwd, grp


app = Flask(__name__)

#Throws OSError exception (it will be thrown when the process is not allowed
#to switch its effective UID or GID):
def drop_privileges():
    if os.getuid() != 0:
        # We're not root so, like, whatever dude
        return

    # Get the uid/gid from the name
    user_name = os.getenv("SUDO_USER")
    pwnam = pwd.getpwnam(user_name)

    # Remove group privileges
    os.setgroups([])

    # Try setting the new uid/gid
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)

    #Ensure a reasonable umask
    old_umask = os.umask(0o22)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route('/run', methods=['POST'])
def run():
    ser = serialconn.open()
    req_json = request.get_json()
    req_cmd = req_json.get('command')
    req_dir = req_json.get('dir')
    if req_cmd:
        if serialconn.login(ser, "kubos", "Kubos123"):
            # Change dir if requested
            if req_dir:
                cmd = "cd %s" % req_dir
                serialconn.send_read_line(ser, cmd)
            resp = serialconn.send_read_line(ser, req_cmd)
            serialconn.close(ser)
            return resp, 200
    return '', 200

@app.route('/flash', methods=['POST'])
def flash():
    ser = serialconn.open()
    req_json = request.get_json()
    req_file = req_json.get('file')
    req_dir = req_json.get('dir')
    if req_file:
        if serialconn.login(ser, "kubos", "Kubos123"):
            if req_dir is None:
                req_dir = "/home/system/usr/local/bin"
            serialconn.send_file(ser, req_file, req_dir)
            return "Transfer of %s complete" % req_file, 200
    return '', 200

@app.cli.command()
def runcmd():
    click.echo("Running test comand")

if __name__ == '__main__':
    print("hello main")
    app.run(host='0.0.0.0')
