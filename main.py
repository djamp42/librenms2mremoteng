import re
import xml.etree.ElementTree as et
import config
from xml.dom import minidom
from apilibrenms import apilibrenms

# Setup LibreNMS API Connection
lnms = apilibrenms.LibrenmsApi(config.librenms_ipaddress, config.librenms_apikey)

# Get dict list of all locations from LibreNMS
librenmsdictlist = lnms.readlocations()

# Create a new list of just the location name, and sort list
listsitesfinal = []
for location in librenmsdictlist:
    listsitesfinal.append(location['location'])
listsitesfinal.sort()
count = 0

# Get site counts for runtime st
# atus
totalsites = len(listsitesfinal)
print("Total Sites: " + str(totalsites))
currentsite = 0


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = et.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


# Setup the root of the element tree
root = et.Element('Connections', {'Name': "Connections",
                                  'Export': "False",
                                  'Protected': 'wjdPzo1TsEdCfIRkAv0sMZlxRqXcc1QdzIyjJy8Hwg7am6jOL9XzS1wVHfkBu9eB',
                                  'ConfVersion': "2.5"
                                  }
                  )

# Start with LibreNMS Import folder
record = config.Record.copy()
record['Name'] = "LibreNMS Import"
record['Type'] = "Container"

librenms_folder = et.SubElement(root, 'Node', record)

# Loop through each location in the librenms list, get list of devices and create location connection folder
for site in listsitesfinal:
    currentsite += 1
    # Build Librenms device search URL based on location.
    # Replace spaces with URL encoded
    # Doesn't work with single quotes, do not use single quotes in librenms location names)
    sitenameurl = re.sub(" ", r"%20", site)
    sitenameurl = re.sub("\'.*", r"", sitenameurl)
    # Get device list based on location
    listdevicelibrenms = lnms.locationsearch(sitenameurl)
    # Stop this loop iteration if no devices for location
    if listdevicelibrenms is None:
        continue
    # Remove LibreNMS Coordinates
    sitename = re.sub("\[.*\]", r"", site)
    # Remove single quotes
    sitename = re.sub(r"'", r"", sitename)
    print(str(currentsite) + "/" + str(totalsites) + "  " + sitename)
    print("    |-----------------------")
    count += 1

    # Create a mremoteng connection for each device.
    createfolder = True
    for device in listdevicelibrenms:
        # Filter devices that are ping os or have no SNMP community
        ignoredevice = [device['os'] == "ping",
                        device['community'] == ""
                        ]
        if any(ignoredevice):
            print("         Ignore Connection: " + device['hostname'] + " / " + device['sysName'])
            continue

        # Check if we already created a folder for this location.
        if createfolder is True:
            # Start Building mremoteNG Site Folder
            folderrecord = config.Record.copy()
            folderrecord['Name'] = sitename
            folderrecord['Type'] = "Container"
            folderrecord['Panel'] = sitename
            folderrecord['InheritPassword'] = "True"
            folderrecord['InheritUsername'] = "True"
            site_folder = et.SubElement(librenms_folder, 'Node', folderrecord)
            createfolder = False

        # Start wish Fresh Record
        record = config.Record.copy()

        # Set mremoteng connection properties
        record['Name'] = f"{device['sysName']}({device['hostname']})"
        record['Type'] = "Connection"
        record['Panel'] = sitename
        record['UserField'] = device['os']
        record['Hostname'] = device['hostname']
        record['ExtApp'] = ""

        # Remove Inheritance for OS types in config.
        if device['os'] in config.noinheritcred:
            record['InheritPassword'] = "False"
            record['InheritUsername'] = "False"

        # Set usernames for OS type in config
        if device['os'] in config.usernamecred:
            for os, username in config.usernamecred.items():
                if device['os'] in os:
                    record['Username'] = username

        # Set Description to device hardware, NA if None
        if device['hardware'] is None:
            record['Descr'] = "NA"
        else:
            record['Descr'] = device['hardware']

        # ICON SECTION

        # Set icon based on OS Type
        if device['os'] in config.firewall_icon:
            record['Icon'] = "Firewall"
        elif device['os'] in config.linux_icon:
            record['Icon'] = "Linux"
        elif device['os'] in config.wifi_icon:
            record['Icon'] = "WiFi"
        elif device['os'] in config.windows_icon:
            record['Icon'] = "Windows"
        elif device['os'] in config.esx_icon:
            record['Icon'] = "ESX"

        # Set icon based on Hardware Type
        for hwarematch in config.switch_icon_hw:
            if re.match(hwarematch, record['Descr']):
                record['Icon'] = "Switch"
        for hwarematch in config.router_icon_hw:
            if re.match(hwarematch, record['Descr']):
                record['Icon'] = "Router"
        for hwarematch in config.wifi_icon_hw:
            if re.match(hwarematch, record['Descr']):
                record['Icon'] = "WiFi"
        for hwarematch in config.vm_icon_hw:
            if re.match(hwarematch, record['Descr']):
                record['Icon'] = "Virtual Machine"

        # Set connection protocol (RDP)
        if device['os'] in config.rdp_dict_os:
            for os, port in config.rdp_dict_os.items():
                if device['os'] in os:
                    record['Protocol'] = "RDP"
                    record['Port'] = port

        # Set connection protocol (Internal HTTPS)
        elif device['os'] in config.internal_https_dict_os:
            for os, port in config.internal_https_dict_os.items():
                if device['os'] in os:
                    record['Protocol'] = "HTTPS"
                    record['Port'] = port

        # Set connection protocol (External HTTPS)
        elif device['os'] in config.extweb_https_dict_os:
            for os, port in config.extweb_https_dict_os.items():
                if device['os'] in os:
                    record['Protocol'] = "IntApp"
                    record['ExtApp'] = config.extweb_https_tool_name
                    record['Port'] = port

        # Set connection protocol (External HTTP)
        elif device['os'] in config.extweb_http_dict_os:
            for os, port in config.extweb_http_dict_os.items():
                if device['os'] in os:
                    record['Protocol'] = "IntApp"
                    record['ExtApp'] = config.extweb_http_tool_name
                    record['Port'] = port

        # Add device to Tree
        print("         Add Connection: " + device['hostname'] + " / " + device['sysName'])
        connection = et.SubElement(site_folder, 'Node', record)


# A hack to get the format of the first line correct. ElementTree.write is hard coded with ' rather than "
data = prettify(root).replace("'", '"')
tmp = data.split('\n')
tmp[0] = '<?xml version="1.0" encoding="utf-8"?>'
with open(f'{config.mremote_cfg_filename}', 'w') as f:
    for line in tmp:
        f.write(line+'\n')
