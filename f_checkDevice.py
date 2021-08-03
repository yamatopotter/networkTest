import os

def getStatus():
    comando = "cat /sys/class/net/eth0/carrier | grep 1"
    response = os.system(comando)

    if (response==0):
        print("Ethernet Up")
        ethCard = True
    else:
        print("Ethernet Down")
        ethCard = False

    comando = "cat /sys/class/net/wlan0/carrier | grep 1"
    response = os.system(comando)

    if(response==0):
        print("Wireless Up")
        wlanCard = True
    else:
        print("Wireless Down")
        wlanCard = False

    return ethCard, wlanCard