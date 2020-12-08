# LibreNMS API Settings
librenms_apikey = ""
librenms_ipaddress = ""

# mremoteng output filename
mremote_cfg_filename = "data\LibreNMS_Import.xml"

# Enter the name of the Web Browser External Tool in mremoteNG
extweb_https_tool_name = "Firefox (HTTPS)"  # Name of External Tool Created in mremoteNG
extweb_http_tool_name = "Firefox (HTTP)"  # Name of External Tool Created in mremoteNG

# OS and Port to use External Web Browser HTTPS (extweb_https_tool_name)
extweb_https_dict_os = {"ruckuswireless-sz": "8443",
                        "ruckuswireless": "443",
                        "ruckuswireless-hotzone": "443",
                        "cimc": "443",
                        "ciscowlc": "443"
                        }

# OS and Port to use External Web Browser HTTP (extweb_http_tool_name)
extweb_http_dict_os = {"pbn": "80"}

# OS and Port to use mremoteNG Internal Web Browser
internal_https_dict_os = {"epmp": "443"}

# OS and Port to use RDP
rdp_dict_os = {"windows": "3389"}

# Icon setting by OS Type. List Librenms OS for each icon type
firewall_icon = ['pfsense']
linux_icon = ['linux']
wifi_icon = ['ciscowlc', "ruckuswireless", "ruckuswireless-sz", "ruckuswireless-hotzone"]
windows_icon = ['windows']
esx_icon = ["vmware"]

# Icon setting by Hardware Type, List Librenms device hardware for each icon type. (REGEX)
switch_icon_hw = ["WS-.*", "cat.*", "Switch System", "MIDPLANE"]
router_icon_hw = ["CISCO2.*", "cisco7.*", "ISR4.*"]
wifi_icon_hw = ["AIR-.*"]
vm_icon_hw = ["ciscoUCVirtualMachine"]

# Inherit Setting, listed OS type that should not have User/Password Inheritance set.
noinheritcred = ['ucos', 'ciscowlc', "linux", "ruckuswireless", "ruckuswireless-sz", "ruckuswireless-hotzone", "vmware"]

# List username for OS type
usernamecred = {"ucos": "administrator",
                "pfsense": "admin",
                "linux": "root",
                "ruckuswireless-hotzone": "admin"
                }

# Default mremoteNG Connection settings
Record = {'Name': "",
          'Type': "Container",
          'Expanded': "False",
          'Descr': "",
          'Icon': "mRemoteNG",
          'Panel': "General",
          'Username': "",
          'Domain': "",
          'Password': "",
          'Hostname': "",
          'Protocol': "SSH2",
          'PuttySession': "Default Settings",
          'Port': "22",
          'ConnectToConsole': "False",
          'UseCredSsp': "True",
          'RenderingEngine': "Gecko",
          'ICAEncryptionStrength': "EncrBasic",
          'RDPAuthenticationLevel': "NoAuth",
          'LoadBalanceInfo': "",
          'Colors': "Colors16Bit",
          'Resolution': "FitToWindow",
          'AutomaticResize': "True",
          'DisplayWallpaper': "False",
          'DisplayThemes': "False",
          'EnableFontSmoothing': "False",
          'EnableDesktopComposition': "False",
          'CacheBitmaps': "False",
          'RedirectDiskDrives': "False",
          'RedirectPorts': "False",
          'RedirectPrinters': "False",
          'RedirectSmartCards': "False",
          'RedirectSound': "DoNotPlay",
          'RedirectKeys': "False",
          'Connected': "False",
          'PreExtApp': "",
          'PostExtApp': "",
          'MacAddress': "",
          'VNCViewOnly': "False",
          'UserField': "",
          'ExtApp': "",
          'VNCCompression': "CompNone",
          'VNCEncoding': "EncHextile",
          'VNCAuthMode': "AuthVNC",
          'VNCProxyType': "ProxyNone",
          'VNCProxyIP': "",
          'VNCProxyPort': "0",
          'VNCProxyUsername': "",
          'VNCProxyPassword': "",
          'VNCColors': "ColNormal",
          'VNCSmartSizeMode': "SmartSAspect",
          'RDGatewayUsageMethod': "Never",
          'RDGatewayHostname': "",
          'RDGatewayUseConnectionCredentials': "Yes",
          'RDGatewayUsername': "",
          'RDGatewayPassword': "",
          'RDGatewayDomain': "",
          'InheritUsername': "True",
          'InheritPassword': "True",
          'InheritCacheBitmaps': "False",
          'InheritColors': "False",
          'InheritDescription': "False",
          'InheritDisplayThemes': "False",
          'InheritDisplayWallpaper': "False",
          'InheritEnableFontSmoothing': "False",
          'InheritEnableDesktopComposition': "False",
          'InheritDomain': "False",
          'InheritIcon': "False",
          'InheritPanel': "False",
          'InheritPort': "False",
          'InheritProtocol': "False",
          'InheritPuttySession': "False",
          'InheritRedirectDiskDrives': "False",
          'InheritRedirectKeys': "False",
          'InheritRedirectPorts': "False",
          'InheritRedirectPrinters': "False",
          'InheritRedirectSmartCards': "False",
          'InheritRedirectSound': "False",
          'InheritResolution': "False",
          'InheritAutomaticResize': "False",
          'InheritUseConsoleSession': "False",
          'InheritUseCredSsp': "False",
          'InheritRenderingEngine': "False",
          'InheritICAEncryptionStrength': "False",
          'InheritRDPAuthenticationLevel': "False",
          'InheritLoadBalanceInfo': "False",
          'InheritPreExtApp': "False",
          'InheritPostExtApp': "False",
          'InheritMacAddress': "False",
          'InheritUserField': "False",
          'InheritExtApp': "False",
          'InheritVNCCompression': "False",
          'InheritVNCEncoding': "False",
          'InheritVNCAuthMode': "False",
          'InheritVNCProxyType': "False",
          'InheritVNCProxyIP': "False",
          'InheritVNCProxyPort': "False",
          'InheritVNCProxyUsername': "False",
          'InheritVNCProxyPassword': "False",
          'InheritVNCColors': "False",
          'InheritVNCSmartSizeMode': "False",
          'InheritVNCViewOnly': "False",
          'InheritRDGatewayUsageMethod': "False",
          'InheritRDGatewayHostname': "False",
          'InheritRDGatewayUseConnectionCredentials': "False",
          'InheritRDGatewayUsername': "False",
          'InheritRDGatewayPassword': "False",
          'InheritRDGatewayDomain': "False"
          }
