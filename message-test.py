from time import sleep
from datetime import datetime
import socket
import corporate_bullshit
# https://github.com/franciscouzo/corporate_bullshit/blob/master/corporate_bullshit.py 

HOST = '139.59.155.101'  # The server's hostname or IP address
PORT = 5678        # The port used by the server

cps = 10 # cycles per second
freq = (1/cps)
print(freq)


def socky():

    lol = "The Chief Sales Technologist prevents our concerns"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(lol.encode())


def test():
    count = 0

    try:
        for i in range(106):
        #while(True):
            timestamp = datetime.now().strftime("%d.%m.%Y %T")
            #print(timestamp + " [notice] : " + corp_bs())
            #s.sendall(lol.encode())
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                #s.sendall(lol.encode())
                s.send((timestamp + " [notice] : " + corp_bs()+'\n').encode())
            count = count +1
            sleep(freq)
            
    except KeyboardInterrupt:
        print(count, 'messages sent at', cps, 'Hz')
    
    print(count, 'messages sent at', cps, 'Hz')


def corp_bs():
    return (corporate_bullshit.sentence())
    

if __name__ == '__main__':
    #socky()
    test()
