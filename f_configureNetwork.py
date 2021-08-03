import os

def disableEthernet():
    comando = "ifconfig eth0 down"
    sudoPass = "<senha do sudo>"
    os.system('echo %s | sudo %s' % (sudoPass, comando))

def enableEthernet():
    comando = "ifconfig eth0 up"
    sudoPass = "<senha do sudo>"
    os.system('echo %s | sudo %s' % (sudoPass, comando))

def disableWireless():
    comando = "ifconfig wlan0 down"
    sudoPass = "<senha do sudo>"
    os.system('echo %s | sudo %s' % (sudoPass, comando))

def enableWireless():
    comando = "ifconfig wlan0 up"
    sudoPass = "<senha do sudo>"
    os.system('echo %s | sudo %s' % (sudoPass, comando))