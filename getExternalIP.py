from requests import get

def getIP():
    resp = '111.111.111.111.'

    while(len(resp)>15):
        ip = get('https://api.ipify.org')
        resp = ip.text
    
    return resp