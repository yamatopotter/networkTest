import f_checkDevice as checkDevice
import f_dbManager as db

eth, wlan = checkDevice.getStatus()

if(eth == False):
    db.insertData('desconexao', "NULL, CURRENT_TIMESTAMP(), eth")

if(wlan == False):
    db.insertData('desconexao', "NULL, CURRENT_TIMESTAMP(), wlan")