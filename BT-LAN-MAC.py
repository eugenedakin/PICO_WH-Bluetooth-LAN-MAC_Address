#This retrieves the MAC Address for both 
#Bluetooth and LAN on a Raspberry Pi Pico W/WH
#Run in Thonny
import bluetooth
import network

# Initialize the WLAN interface in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Get the LAN MAC address
lan_mac = wlan.config('mac')

# Convert it to a human-readable format
lan_mac_address = ':'.join('%02X' % b for b in lan_mac)
print("LAN MAC Address:", lan_mac_address)

# Activate Bluetooth
bt = bluetooth.BLE()
bt.active(True)

# Get the Bluetooth MAC address
mac = bt.config('mac')
mac_bytes = mac[1]

#Convert to human readable format
mac_str = ':'.join('%02X' %b for b in mac_bytes)
bt_mac_address = ':'.join('%02X' % b for b in mac_bytes)
print("Bluetooth MAC Address", bt_mac_address)
