# PICO_WH-Bluetooth-LAN-MAC_Address
Gets MAC Address on Pico WH for Bluetooth and LAN

First we need to setup the Raspberry Pi 5 virtual environment. Type the following two commands in a terminal:
1)	On the Raspberry PI 5:
a.	Make a new folder called Pico-Pi5 (/home/DakServer/Desktop/Bluetooth/Pico-Pi5)
b.	Create a virtual environment (python3 -m venv venv)
c.	Activate virtual environment (source venv/bin/activate)
d.	Install bleak library (pip install bleak)
2)	Setup Raspberry Pi Pico (https://www.kevsrobots.com/learn/how_to_install_micropython/)
a.	Ensure the IDE thonny is installed on the Raspberry Pi 5
b.	Hold down the boot button and plug it into the Raspberry PI 5, this puts the pico wh in bootloader mode
c.	Open thonny and select pico from the list of devices
d.	Install micropython
i.	Micropython family = RP2
ii.	Variant = Pico WH
iii.	Press Install button

