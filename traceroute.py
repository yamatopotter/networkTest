import os
import f_checkDevice as checkDevice
import f_dbManager as db

hostnames = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]
lastResponse = ["dns.google", "dns.google", "one.one.one"]

#Ethernet
def traceroute():
    eth, wlan = checkDevice.getStatus()
    
    if(eth == True):
        i = 0
        for hostname in hostnames:
            print("Iniciando traceroute ao servidor "+hostname)
            comando = "traceroute -i eth0 "+ hostname+" | grep "+lastResponse[i]
            response = os.system(comando)
            if(response==256):
                dadosDb = "NULL, CURRENT_TIMESTAMP(), '{host}', {sucesso}, 0".format(host = hostname, sucesso=0)
                db.insertData('traceroute_avg', dadosDb)
                db.insertData('traceroute_total', dadosDb)
            else:
                dadosDb = "NULL, CURRENT_TIMESTAMP(), '{host}', {sucesso}, 0".format(host = hostname, sucesso=1)
                db.insertData('traceroute_avg', dadosDb)
                db.insertData('traceroute_total', dadosDb)
            i+=1
    else:
        print("Parece que a interface Ethernet está desconectada")
        eth = 0

    if (wlan==True):
        i=0
        for hostname in hostnames:
            print("Iniciando traceroute ao servidor "+hostname)
            comando = "traceroute -i wlan0 "+ hostname+" | grep "+lastResponse[i]
            response = os.system(comando)
            if(response==256):
                dadosDb = "NULL, CURRENT_TIMESTAMP(), '{host}', {sucesso}, 1".format(host = hostname, sucesso=0)
                db.insertData('traceroute_avg', dadosDb)
                db.insertData('traceroute_total', dadosDb)
            else:
                dadosDb = "NULL, CURRENT_TIMESTAMP(), '{host}', {sucesso}, 1".format(host = hostname, sucesso=1)
                db.insertData('traceroute_avg', dadosDb)
                db.insertData('traceroute_total', dadosDb)
            i+=1
    else:
        print("Parece que a interface Wireless está desconectada")
        wlan = 0

traceroute()