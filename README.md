# LibreNMS 2 MRemoteNG

This scripts grabs a list of all locations in LibreNMS and creates a MRemoteNG Connection File. 
You can then import this file into MRemoteNG.

* Creates a folder for each location in LibreNMS
* Adds all devices in that location to the folder.
* Set device connection icons, Protocol, username, and type per config.py 
* Inheritance is set so you can set the username/password for all devices on the main LibreNMS import forlder.
* config.example.py has most of the stuff you will want to customize.

# Notes
* Passwords cannot be set, MRemoteNG encrypts passwords and i do not know how they do this
* Devices without SNMP or PING only are ignored and not added. 

# Install
1) Install my apilibrenms library
`pip3 install git+https://github.com/djamp42/apilibrenms`
    
2) Create new folder and clone repo into it.
`git clone https://github.com/djamp42/librenms2mremoteng`

3) Rename config.example.py to config.py.

4) Set librenms_apikey and librenms_ipaddress in config.py

# Usage
**python ./main.py**
This will output the librenms connection file to the data subdirectory
