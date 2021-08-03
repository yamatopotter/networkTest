import subprocess
import f_checkDevice as checkDevice
import f_dbManager as db

def speedTestCommand(interface):
    comando = "speedtest -I {interface}".format(interface = interface)
    getOutput = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout
    output = getOutput.read()
    return output

def get_conection_info():

    eth,wlan = checkDevice.getStatus()

    if(eth==1):
        saida = speedTestCommand('eth0')

        saida = saida.decode('UTF-8') # Pra ficar bonitinho
        saida = saida.strip('\n') # Removendo essas quebras de linha desnecessárias no começo e no final
        saida = saida.split('\n') # Separando por linhas

        dadosEth = {} # Dicionario vazio

        for i in range(len(saida)):
            # Se tem um ':' é pq tem algum dado importante
            if ':' in saida[i]:
                # Procurando o ':' pra separar chave e valor
                ind = saida[i].find(':')
                saida[i] = [
                    saida[i][:ind].strip(), # A chave e tudo que tem antes do primeiro ':'
                    saida[i][ind+1:].strip() # O valor e tudo o que vem depois
                    ]
                # Adicionando a chave e o valor em um dicionario
                dadosEth[saida[i][0]] = saida[i][1]

        # Tratando da latência
        aux = dadosEth['Latency']

        latency = aux.find('ms')
        latency = aux[:latency-1]
        latency = float(latency)

        ind1 = aux.find('(')
        ind2 = aux.find('ms', ind1)

        jitter = aux[ind1+1:ind2-1]
        jitter = float(jitter)

        dadosEth['Latency'] = {'delay': latency, 'jitter': jitter}


        # Tratando da velocidade de download
        aux = dadosEth['Download']
        ind = aux.find('Mbps')
        download = aux[:ind-1]
        download = float(download)
        dadosEth['Download'] = download

        # Tratando da velocidade de upload
        aux = dadosEth['Upload']
        ind = aux.find('Mbps')
        upload = aux[:ind-1]
        upload = float(upload)
        dadosEth['Upload'] = upload


        # Tratando do packet loss
        aux = dadosEth['Packet Loss']
        if 'Not available' in aux:
            dadosEth['Packet Loss'] = 0

        # Printando no console
        #for key in dados:
        #    print("{}: {}".format(key, dados[key]))       
    else:
        dadosEth={
            'ISP': 'Offline',
            'Server': 'Offline',
            'Download': 0.0,
            'Upload': 0.0,
            'Latency':{
                'jitter':20,
                'delay':100
            }
        }

    if(wlan==1):
        saida = speedTestCommand('wlan0')

        saida = saida.decode('UTF-8') # Pra ficar bonitinho
        saida = saida.strip('\n') # Removendo essas quebras de linha desnecessárias no começo e no final
        saida = saida.split('\n') # Separando por linhas

        dadosWlan = {} # Dicionario vazio

        for i in range(len(saida)):
            # Se tem um ':' é pq tem algum dado importante
            if ':' in saida[i]:
                # Procurando o ':' pra separar chave e valor
                ind = saida[i].find(':')
                saida[i] = [
                    saida[i][:ind].strip(), # A chave e tudo que tem antes do primeiro ':'
                    saida[i][ind+1:].strip() # O valor e tudo o que vem depois
                    ]
                # Adicionando a chave e o valor em um dicionario
                dadosWlan[saida[i][0]] = saida[i][1]

        # Tratando da latência
        aux = dadosWlan['Latency']

        latency = aux.find('ms')
        latency = aux[:latency-1]
        latency = float(latency)

        ind1 = aux.find('(')
        ind2 = aux.find('ms', ind1)

        jitter = aux[ind1+1:ind2-1]
        jitter = float(jitter)

        dadosWlan['Latency'] = {'delay': latency, 'jitter': jitter}


        # Tratando da velocidade de download
        aux = dadosWlan['Download']
        ind = aux.find('Mbps')
        download = aux[:ind-1]
        download = float(download)
        dadosWlan['Download'] = download

        # Tratando da velocidade de upload
        aux = dadosWlan['Upload']
        ind = aux.find('Mbps')
        upload = aux[:ind-1]
        upload = float(upload)
        dadosWlan['Upload'] = upload


        # Tratando do packet loss
        aux = dadosWlan['Packet Loss']
        if 'Not available' in aux:
            dadosWlan['Packet Loss'] = 0

        # Printando no console
        #for key in dados:
        #    print("{}: {}".format(key, dados[key]))       
    else:
        dadosWlan={
            'ISP': 'Offline',
            'Server': 'Offline',
            'Download': 0.0,
            'Upload': 0.0,
            'Latency':{
                'jitter':20,
                'delay':100
            }
        }

    return dadosEth, dadosWlan

resultEth, resultWlan = get_conection_info()
print(resultEth)
print(resultWlan)

#Inserção dos dados da porta Ethernet
dadosDb = "NULL, CURRENT_TIMESTAMP(), {download}, {upload}, {jitter}, {delay}, '{isp}', '{server}', 0".format(download = resultEth['Download'], upload = resultEth['Upload'], jitter = resultEth['Latency']['jitter'], delay = resultEth['Latency']['delay'], isp = resultEth['ISP'], server = resultEth['Server'])
db.insertData('velocidade', dadosDb)

#Inserção dos dados na porta Wireless
dadosDb = "NULL, CURRENT_TIMESTAMP(), {download}, {upload}, {jitter}, {delay}, '{isp}', '{server}', 1".format(download = resultWlan['Download'], upload = resultWlan['Upload'], jitter = resultWlan['Latency']['jitter'], delay = resultWlan['Latency']['delay'], isp = resultWlan['ISP'], server = resultWlan['Server'])
db.insertData('velocidade', dadosDb)
