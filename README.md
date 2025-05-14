# PICO_WH-Bluetooth-LAN-MAC_Address
Gets MAC Address on Pico WH for Bluetooth and LAN

First we need to setup the Raspberry Pi 5 virtual environment. Type the following two commands in a terminal:
1)	On the Raspberry PI 5:
 - Make a new folder called Pico-Pi5 (/home/PiServerName/Desktop/Bluetooth/Pico-Pi5)
 - Create a virtual environment (python3 -m venv venv)
 - Activate virtual environment (source venv/bin/activate)
 - Install bleak library (pip install bleak)
2)	Setup Raspberry Pi Pico 
 - Ensure the IDE thonny is installed on the Raspberry Pi 5
 - Hold down the boot button and plug it into the Raspberry PI 5, this puts the pico wh in bootloader mode
 - Open thonny and select pico from the list of devices
 - Install micropython, select the following options:
 - Micropython family = RP2
 - Variant = Pico WH
 - Press Install button
3) Open the python file BT-LAN-MAC.py from the gihub, and run it in the Thonny IDE. At the bottom of the Thonny IDE, the data should look like the following:
   
![](https://github.com/eugenedakin/PICO_WH-Bluetooth-LAN-MAC_Address/blob/main/PicoWH-BT-LAN-ScreenGrab.png)
