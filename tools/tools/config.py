import yaml

CONFIG_FILE = "/home/vagrant/.kubos/debug.yml"

try:
    with open(CONFIG_FILE, 'r') as ymlfile:
      cfg = yaml.load(ymlfile)
except:
    cfg = {}

# Default to a local server
IP = "127.0.0.1"
PORT = 52861

if 'IP' in cfg:
    IP = cfg['IP']

if 'PORT' in cfg:
    PORT = cfg['PORT']

URL = "http://%s:%d" % (IP, PORT)
