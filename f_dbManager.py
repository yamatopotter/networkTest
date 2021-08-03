import mysql.connector
db = ''
cursor = ''

def dbConnect():
    global db, cursor
    db = mysql.connector.connect(
            host="<host>",
            user="<usuario>",
            password = "<senha>",
            database= "network_data"
    )

    cursor = db.cursor()

def insertData(table, values):
    global cursor, db

    dbConnect()
    cursor.execute("INSERT INTO {} VALUES ({})".format(table, values))
    db.commit()
    db.close()

def getFirstData():
    global cursor, db

    dbConnect()

    sql = "SELECT data FROM ping_avg LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    db.close()

    for row in result:
        data = (row[0])
    
    return data

def avgData(table, select, function, where):
    global cursor, db

    dbConnect()

    if (where == ''):
        sql = "SELECT {} FROM {}".format(select, table)
        print(sql)
        cursor.execute(sql)
    else:
        sql = "SELECT {} FROM {} WHERE {}".format(select, table, where)
        print(sql)
        cursor.execute(sql)

    result = cursor.fetchall()
    
    db.close()

    if(function == 'ping'):
        avgPerda = []
        avgSucesso = []
        avgRecebidos = []

        for row in result:
            avgPerda.append(row[0])
            avgSucesso.append(row[1])
            avgRecebidos.append(row[2])

        dados = {}

        dados['Perda'] = sum(avgPerda)/len(avgPerda)
        dados['Sucesso'] = (sum(avgSucesso)/len(avgSucesso))
        dados['Recebidos'] = sum(avgRecebidos)/len(avgRecebidos)
    elif (function == 'traceroute'): 
        avgSucesso = []

        for row in result:
            avgSucesso.append(row[0])
        
        dados = (sum(avgSucesso)/len(avgSucesso))
    elif (function == 'speedAvg'):
        avgDownload = []
        avgUpload = []
        avgJitter = []
        avgPing = []

        for row in result:
            avgDownload.append(row[0])
            avgUpload.append(row[1])
            avgJitter.append(row[2])
            avgPing.append(row[3])

        dados = {}
        dados['Download'] = (sum(avgDownload)/len(avgDownload))
        dados['Upload'] = (sum(avgUpload)/len(avgUpload))
        dados['Jitter'] = (sum(avgJitter)/len(avgJitter))
        dados['Delay'] = (sum(avgPing)/len(avgPing))

    else:
        avgDownload = []
        avgUpload = []
        avgJitter = []
        avgPing = []
        isp = ''
        host = ''

        for row in result:
            avgDownload.append(row[0])
            avgUpload.append(row[1])
            avgJitter.append(row[2])
            avgPing.append(row[3])
            isp = row[4]
            host = row[5]

        dados = {}
        dados['Download'] = (sum(avgDownload)/len(avgDownload))
        dados['Upload'] = (sum(avgUpload)/len(avgUpload))
        dados['Jitter'] = (sum(avgJitter)/len(avgJitter))
        dados['Delay'] = (sum(avgPing)/len(avgPing))
        dados['ISP'] = isp
        dados['Host'] = host
        
    return dados

def checkLanStability():
    global cursor, db

    dbConnect()

    cursor.execute("SELECT data, interface FROM desconexao")
    result = cursor.fetchall()

    db.close()

    return result

def truncateTable(table):
    global cursor, db

    dbConnect()

    cursor.execute("Truncate {}".format(table))

    db.commit()  
    db.close()
