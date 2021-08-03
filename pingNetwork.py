import subprocess
import f_dbManager as db
import f_checkDevice as checkDevice

hostnames = ["8.8.8.8", "8.8.4.4", "1.1.1.1", '208.67.222.222']

def pingNetwork(packets):
    eth, wlan = checkDevice.getStatus()

    if(eth == True):
        print("Pinging Ethernet")
        for hostname in hostnames:
            comando = "ping -s 16 -c "+str(packets)+" -I eth0 "+hostname
            getOutput = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout
            ping = getOutput.read()
            perdidos = str(ping)
            recebidos = str(ping)

            # perda de pacote
            aux = perdidos.find('packet loss')

            perdidos = perdidos[aux-10:aux]
            perdidos = perdidos.split()[-1]
            perdidos = perdidos[:-1]

            perda = int(perdidos) #número de 0 a 100

            # pacotes recebidos
            aux = recebidos.find('received')

            recebidos = recebidos[aux-5:aux]
            recebidos = recebidos.split()[-1]

            chegou = int(recebidos)

            print("Host: "+hostname)
            print("Perda de pacotes: "+str(perda))
            print("Pacotes recebidos: "+str(chegou))

            pctSucesso = (chegou/15)

            print("Porcentagem de Sucesso: "+ str(pctSucesso) +"%")

            dadosDb = "NULL, {perda}, {sucesso}, {recebidos}, CURRENT_TIMESTAMP(), '{server}', 0 ".format(perda = perda, sucesso = pctSucesso, recebidos = chegou, server = hostname)
            db.insertData('ping_avg', dadosDb)
            db.insertData('ping_total', dadosDb)
            
    else:
        print("Parece que a interface com fio está desconectada")
    
    if(wlan == True):    
        print("Pinging Wireless")

        for hostname in hostnames:
            comando = "ping -s 16 -c "+str(packets)+" -I wlan0 "+hostname
            getOutput = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout
            ping = getOutput.read()
            perdidos = str(ping)
            recebidos = str(ping)

            # perda de pacote
            aux = perdidos.find('packet loss')

            perdidos = perdidos[aux-10:aux]
            perdidos = perdidos.split()[-1]
            perdidos = perdidos[:-1]

            perda = int(perdidos) #número de 0 a 100

            # pacotes recebidos
            aux = recebidos.find('received')

            recebidos = recebidos[aux-5:aux]
            recebidos = recebidos.split()[-1]

            chegou = int(recebidos)

            print("Host: "+hostname)
            print("Perda de pacotes: "+str(perda))
            print("Pacotes recebidos: "+str(chegou))

            pctSucesso = (chegou/15)

            print("Porcentagem de Sucesso: "+ str(pctSucesso) +"%")
            
            dadosDb = "NULL, {perda}, {sucesso}, {recebidos}, CURRENT_TIMESTAMP(), '{server}', 1 ".format(perda = perda, sucesso = pctSucesso, recebidos = chegou, server = hostname)
            db.insertData('ping_avg', dadosDb)
            db.insertData('ping_total', dadosDb)
    else:
        print("Parece que a interface sem fio está desconectada")

    # return ethPerda, ethRecebidos, ethSucesso, wlanPerda, wlanRecebidos, wlanSucesso

pingNetwork(15)