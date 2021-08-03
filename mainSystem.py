import pingNetwork
import traceroute
import getExternalIP
import internetSpeed
import configureNetwork
import checkDevice
import sendStatistic
from datetime import datetime
import time

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Variaveris Gerais
ipCliente = 0

# Variaveis de Funcionamento das Interfaces
ethCard = False
wlanCard = False

# Variaveis do comando Ping
# lossEth = []
# successEth = []
percEth = []
# lossWlan = []
# successWlan = []
percWlan = []

# Variaveis do comando Traceroute
tracertEthernet = []
tracertWireless = []

# Variaveis do speedTest
speedTestEth = []
speedTestWlan = []

#Avg
avgSuccessPingEth = []
avgSuccessPingWlan = []
avgSuccessTracertEth = []
avgSuccessTracertWlan = []
avgSpeed = 0

#Total
totalSuccessPingEth = []
totalSuccessPingWlan = []
totalSuccessTracertEth = []
totalSuccessTracertWlan = []
totalSpeed = []

def verificarDispositivo():
    global ethCard, wlanCard

    print("Verificando dispositivos ...")
    ethCard, wlanCard = checkDevice.getStatus()

def ipExterno():
    global ipCliente

    print("Pegando IP")
    ipCliente = getExternalIP.getIP()

def pingRede():
    global percEth, percWlan, avgSuccessPingEth, avgSuccessPingWlan, totalSuccessPingEth, totalSuccessPingWlan

    print("Iniciando Ping")
    percEth, percWlan = pingNetwork.pingNetwork(15,ethCard,wlanCard)
    
    avgSuccessPingEth.extend(percEth)
    avgSuccessPingWlan.extend(percWlan)
    totalSuccessPingEth.extend(percEth)
    totalSuccessPingWlan.extend(percWlan)

def tracerouteRede():
    global avgSuccessPingEth, avgSuccessPingWlan, avgSuccessTracertEth, avgSuccessTracertWlan, totalSuccessTracertEth, totalSuccessTracertWlan

    print("Iniciando Traceroute")
    
    avgPingEth = sum(avgSuccessPingEth) / len(avgSuccessPingEth)
    if(avgPingEth>70):
        tracertEthernet = traceroute.tracerouteEthernet(ethCard)
        avgSuccessTracertEth.extend(tracertEthernet)
        totalSuccessTracertEth.extend(tracertEthernet)

    avgPingWlan = sum(avgSuccessPingWlan) / len(avgSuccessPingWlan)
    if(avgPingWlan>70):
        tracertWireless = traceroute.tracerouteWireless(wlanCard)
        avgSuccessTracertWlan.extend(tracertWireless)
        totalSuccessTracertWlan.extend(tracertWireless)
        
def testeVelocidade():
    global avgSpeed, totalSpeed

    print("Medição da velocidade")
    speed = internetSpeed.internetSpeed()
    avgSpeed = round(float(speed),2)
    totalSpeed.append(round(float(speed),2))

def createStatistic():
    global avgSuccessPingEth, avgSuccessPingWlan, avgSuccessTracertEth, avgSuccessTracertWlan, totalSuccessPingEth, totalSuccessPingWlan, totalSuccessTracertEth, totalSuccessTracertWlan, totalSpeed, avgSpeed, ipCliente, dt_string

    # Calculo das médias
    avgPingEth = (sum(avgSuccessPingEth)/len(avgSuccessPingEth)) / 100
    avgPingWlan =  (sum(avgSuccessPingWlan)/len(avgSuccessPingWlan)) / 100
    avgTracerouteEth = sum(avgSuccessTracertEth)/len(avgSuccessTracertEth)
    avgTracerouteWlan = sum(avgSuccessTracertWlan)/len(avgSuccessTracertWlan)

    totalAvgPingEth = (sum(totalSuccessPingEth)/len(totalSuccessPingEth)) / 100
    totalAvgPingWlan = (sum(totalSuccessPingWlan)/len(totalSuccessPingWlan)) / 100
    totalAvgTracerouteEth = sum(totalSuccessTracertEth)/len(totalSuccessTracertEth)
    totalAvgTracerouteWlan = sum(totalSuccessTracertWlan)/len(totalSuccessTracertWlan)

    totalAvgSpeed = sum(totalSpeed)/len(totalSpeed)

    sendStatistic.sendMail(avgPingEth, avgPingWlan,avgTracerouteEth, avgTracerouteWlan, totalAvgPingEth, totalAvgPingWlan, totalAvgTracerouteEth, totalAvgTracerouteWlan, avgSpeed, totalAvgSpeed, dt_string, ipCliente)

    print("Relatório temporal \n\n")

    print("Meu IP: " + str(ipCliente))
    print("Ping Ethernet: "+str(avgPingEth)+ "%")
    print("Ping Wireless: "+str(avgPingWlan)+ "%")
    print("Traceroute da Ethernet: " + str(avgTracerouteEth) + "%")
    print("Traceroute da Wireless: " + str(avgTracerouteWlan)+ "%")
    print("Velocidade da Internet: " + str(avgSpeed) + "Mbit/s \n\n")

    print("Relatório total \n\n")

    print("Ping Ethernet: "+str(totalAvgPingEth)+ "%")
    print("Ping Wireless: "+str(totalAvgPingWlan)+ "%")
    print("Traceroute da Ethernet: " + str(totalAvgTracerouteEth) + "%")
    print("Traceroute da Wireless: " + str(totalAvgTracerouteWlan)+ "%")
    print("Velocidade da Internet: " + str(totalAvgSpeed) + "Mbit/s \n\n")

    avgSuccessPingEth.clear()
    avgSuccessPingWlan.clear()
    avgSuccessTracertEth.clear()
    avgSuccessTracertWlan.clear()
    avgSpeed=0
    ipCliente=0

#Inicio do programa principal

#verificação dos dispositivos físicos
verificarDispositivo()
#captura do ip Externo
ipExterno()

#realização de testes de ping e traceroute
for i in range(2):
    pingRede()
    tracerouteRede()    
testeVelocidade()
createStatistic()