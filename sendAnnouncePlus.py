import requests
#import sys
import Torrent
import socket



def sendAnnounce(torrent,pid,downloadedFile,mode,uploaded,sock,leave):
    

    piecesStatus = ''
    amtLeft = 0 
    amtDown = 0
    for piece in downloadedFile:
        if piece == None:
            piecesStatus += '0'
            amtLeft += 1
        else:
            piecesStatus += '1'
            amtDown += 1
    if leave == True:
        amtLeft = -1 #this means that we're leaving the swarm

    PARAMS = {
                'info_hash': str(torrent.info_hash),
                'peer_id': pid,
                'port': sock[1],
                'uploaded': uploaded,
                'downloaded': amtDown,
                'left': amtLeft,
                'ip':sock[0],
                #'compact': 1,
                'mode': mode,
                'piecesStatus': piecesStatus
                }

    r = requests.get(url=torrent.announce,params=PARAMS)
    if r.text[0:5] == 'ERROR':
        print(r.text)
        return []
    temp = r.text[:-1]
    
    temp2 = temp.split(',')
    temp3 = []
    for ele in temp2:
        temp3.append(ele.split(':'))
    return (temp3)

    #print (r)
    #print (r.text)
    #print (r.url)
    #print (r.status_code)
