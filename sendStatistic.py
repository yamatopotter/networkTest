import smtplib, ssl
import getExternalIP as ipTool
import f_dbManager as db

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 465
password = "<senha do email>"
sender_email = "<email de envio>"
receiver_email = "<email receptor>"

def sendMail():
    global port, password, sender_email, receiver_email
    
    ipExterno = ipTool.getIP()

    now = datetime.now()
    # dd/mm/YY H:M:S
    ultimaData = now.strftime("%d/%m/%Y %H:%M:%S")
    dataInicial = db.getFirstData()

    msg = MIMEMultipart("alternative")

    # Ping Ethernet

    dados = {}
    dados = db.avgData('ping_avg', "perda, sucesso, recebidos", 'ping', 'interface = 0')
    
    pingEth = dados['Sucesso']

    dados = {}
    dados = db.avgData('ping_total', "perda, sucesso, recebidos", 'ping', 'interface = 0')

    avgPingEth = dados['Sucesso']

    # Ping Wireless

    dados = {}
    dados = db.avgData('ping_avg', "perda, sucesso, recebidos", 'ping', 'interface = 1')
    
    pingWlan = dados['Sucesso']

    dados = {}
    dados = db.avgData('ping_total', "perda, sucesso, recebidos", 'ping', 'interface = 1')

    avgPingWlan = dados['Sucesso']

    # Traceroute Ethernet

    dados = 0 
    dados = db.avgData('traceroute_avg', "sucesso", 'traceroute', 'interface = 0')
    
    tracerouteEth = dados

    dados = 0 
    dados = db.avgData('traceroute_total', "sucesso", 'traceroute', 'interface = 0')

    avgTracerouteEth = dados

    # Traceroute Wireless

    dados = 0 
    dados = db.avgData('traceroute_avg', "sucesso", 'traceroute', 'interface = 1')
    
    tracerouteWlan = dados

    dados = 0 
    dados = db.avgData('traceroute_total', "sucesso", 'traceroute', 'interface = 1')

    avgTracerouteWlan = dados

    #Ultimo Speedtest Ethernet

    dados = 0
    dados = db.avgData('velocidade', "download, upload, jitter, delay, isp, server", 'speed', 'id = (SELECT id FROM velocidade WHERE interface = 0 ORDER BY id DESC LIMIT 1)')
    
    avgDownloadEth = dados['Download']
    avgUploadEth = dados['Upload']
    avgJitterServerEth = dados['Jitter']
    avgPingServerEth = dados['Delay']
    ispEth = dados['ISP']
    hostEth = dados['Host']

    #Avg SpeedTest Ethernet

    dados = 0
    dados = db.avgData('velocidade', "download, upload, jitter, delay", 'speedAvg', 'interface = 0')
    
    downloadEth = dados['Download']
    uploadEth = dados['Upload']
    jitterServerEth = dados['Jitter']
    pingServerEth = dados['Delay']


    #Ultimo Speedtest Wireless

    dados = 0
    dados = db.avgData('velocidade', "download, upload, jitter, delay, isp, server", 'speed', 'id = (SELECT id FROM velocidade WHERE interface = 1 ORDER BY id DESC LIMIT 1)')
    
    avgDownloadWlan = dados['Download']
    avgUploadWlan = dados['Upload']
    avgJitterServerWlan = dados['Jitter']
    avgPingServerWlan = dados['Delay']
    ispWlan = dados['ISP']
    hostWlan = dados['Host']

    #Avg SpeedTest Wireless

    dados = 0
    dados = db.avgData('velocidade', "download, upload, jitter, delay", 'speedAvg', 'interface = 1')
    
    downloadWlan = dados['Download']
    uploadWlan = dados['Upload']
    jitterServerWlan = dados['Jitter']
    pingServerWlan = dados['Delay']

    # Desconex??es

    relatorioQueda = ''
    dados = db.checkLanStability()

    if (len(dados)>0):
        for aux in dados:
            relatorioQueda += "{data} - {interface}\n".format(data = aux[0], interface = aux[1])  
    else:
        relatorioQueda = "N??o houve quedas nas redes at?? o envio do relat??rio"

    # Cabe??alho da mensagem
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Relat??rio de Monitoramento de Rede - NS"

    # Data/Hora de inicio: {dtHoraInicio}\n
    # Data/Hora de envio: {dtHora}\n

    message = '''\
    Data de inicio temporal: {dataTemporal}
    Data de montagem do relat??rio: {dataFinal}

    Ip externo do teste: {ipExterno}\n
    -------- Estat??stica de Ping --------\n

    Estat??stica de Ping Ethernet temporal: {pingEth:.2%}  
    Estatistica de Ping Ethernet total: {avgPingEth:.2%}\n

    Estat??stica de Ping Wireless temporal: {pingWlan:.2%}  
    Estat??stica de Ping Wireless total: {avgPingWlan:.2%}\n

    -------- Estatistica de Rota --------\n

    Estat??stica de Rota Ethernet temporal: {tracerouteEth:.2%}    
    Estat??stica de Rota Ethernet total: {avgTracerouteEth:.2%}\n

    Estat??stica de Rota Wireless temporal: {tracerouteWlan:.2%}   
    Estat??stica de Rota Wireless total: {avgTracerouteWlan:.2%}\n

    ----- Estat??stica de Velocidade Ethernet -----\n
    Provedor de internet: {ispEth}
    Host Utilizado para teste: {hostEth}

    Estat??stica de Download temporal: {avgDownloadEth:.2f} Mbps   
    Estat??stica de Download total: {downloadEth:.2f} Mbps\n

    Estat??stica de Upload temporal: {avgUploadEth:.2f} Mbps   
    Estat??stica de Upload total: {uploadEth:.2f} Mbps\n
    
    Estat??stica de Ping temporal: {avgPingServerEth:.2f}ms
    Estatistica de Ping total: {pingServerEth:.2f}ms\n

    Estat??stica de Jitter temporal: {avgJitterServerEth:.2f}ms
    Estat??stica de Jitter total: {jitterServerEth:.2f}ms\n

    ----- Estat??stica de Velocidade Wireless -----\n
    Provedor de internet: {ispWlan}
    Host Utilizado para teste: {hostWlan}\n

    Estat??stica de Download temporal: {avgDownloadWlan:.2f} Mbps   
    Estat??stica de Download total: {downloadWlan:.2f} Mbps\n

    Estat??stica de Upload temporal: {avgUploadWlan:.2f} Mbps   
    Estat??stica de Upload total: {uploadWlan:.2f} Mbps\n
    
    Estat??stica de Ping temporal: {avgPingServerWlan:.2f}ms
    Estatistica de Ping total: {pingServerWlan:.2f}ms\n

    Estat??stica de Jitter temporal: {avgJitterServerWlan:.2f}ms
    Estat??stica de Jitter total: {jitterServerWlan:.2f}ms

    ----- Relat??rio de Estabilidade LAN -----\n

    {relatorioQueda}

    '''.format(dataTemporal = dataInicial, dataFinal = ultimaData, ipExterno = ipExterno, pingEth = pingEth, avgPingEth = avgPingEth, pingWlan = pingWlan, avgPingWlan = avgPingWlan, tracerouteEth = tracerouteEth, avgTracerouteEth = avgTracerouteEth, tracerouteWlan = tracerouteWlan, avgTracerouteWlan = avgTracerouteWlan, ispEth = ispEth, hostEth = hostEth, avgDownloadEth = avgDownloadEth, downloadEth = downloadEth, avgUploadEth=avgUploadEth, uploadEth = uploadEth, avgPingServerEth = avgPingServerEth, pingServerEth = pingServerEth, avgJitterServerEth = avgJitterServerEth, jitterServerEth = jitterServerEth, ispWlan = ispWlan, hostWlan = hostWlan, avgDownloadWlan = avgDownloadWlan, downloadWlan = downloadWlan, avgUploadWlan = avgUploadWlan, uploadWlan = uploadWlan, avgPingServerWlan = avgPingServerWlan, pingServerWlan = pingServerWlan, avgJitterServerWlan = avgJitterServerWlan, jitterServerWlan = jitterServerWlan, relatorioQueda = relatorioQueda)

    #message = message.decode('UTF-8')

    msg.attach(MIMEText(message, 'plain'))


    # Estatistica de Rota Wireless temporal: {tracerouteWlan:.2}\n    
    # Estatistica de Rota Wireless total: {avgTracerouteWlan:.2}\n\n

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.zoho.com", port, context=context) as server:
        server.login("noreply@apolloit.com.br", password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    db.truncateTable('ping_avg')
    db.truncateTable('traceroute_avg')
    db.truncateTable('desconexao')

sendMail()
