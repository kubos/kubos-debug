Kubos SDK Debugging Tools
==========================

This project contains simple debugging tools designed to supplement the Kubos SDK. These tools are specifically for working with devices over a serial console.

Tooling Architecture
---------------------
This tooling project is broken up into two major parts:

 - Server - Handles communications with embedded device
 - Tools - Specific tools/commands to run against the device

Currently only two commands are supported:

 - Run - runs a designated command on the device
 - Flash - Loads a designated file on the device

Usage
-----

First step is to clone this repo.

Starting the server
~~~~~~~~~~~~~~~~~~~

You will need to have Python3, Flask, Gunicorn and Pyserial installed to run the server. If you already have Python3/Pip3 installed then you can get the other dependencies with this command::

    pip3 install Flash gunicorn pyserial

The server is started by running `./run.sh` from within the `server` folder. By default the server will be bound to `0.0.0.0:52861`.

The server also assumes that your serial device is presented as `/dev/ttyUSB0` and is using the default kubos login/password. 

Installing the tools
~~~~~~~~~~~~~~~~~~~~

The tools can be installed by running this command::

    pip install .

Run this command from the `tools` folder of the repo.

.. note::
  
    Make sure that your PATH includes the folder where `pip` places binaries.

Running the tools
~~~~~~~~~~~~~~~~~

The tools communicate with the server over HTTP to send their command and receive the response. The tools must be run in an environment where they can reach the server.

The server could be running locally or on a shared machine.
Specifying the server ip/port is done through a local configuration file. Right now the tools look for that config file at `/home/vagrant/.kubos/config.yml`. The config file currently has just two options, IP and PORT. 

Example:

.. code-block:: yaml
    
    IP: 192.168.1.205
    PORT: 52861

Currently the two tools are `debug_run` and `debug_flash`.

The `debug_run` takes a command and an optional directory to execute the command in. If the directory is not included then the command will be run in whatever the current working directory is. The command will return back output from the device.

Examples:

::

    debug_run ls
    debug_run ls -d /etc
    debug_run "cat passwd" -d /etc

The `debug_flash` takes a file path and an optional destination directory for that file. If the directory is not included then the file will be transferred to `/home/system/usr/local/bin`. It will wait until the file has been transferred to the device and return back a success or failure message.

Examples:

::

    debug_flash testprog
    debug_flash network_config /etc/network


