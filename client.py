import socket
import sys


class Client:
    # UDP_IP = '192.168.1.30'
    # UDP_PORT = 5000
    #
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    # sock.bind((UDP_IP, UDP_PORT))
    #
    # while True:
    #     data, addr = sock.recvfrom(1024)
    #     print('received message:', data.decode())

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print('Failed to create socket')
        sys.exit()
    host = input('Enter host: ')
    port = 5000

    while True:
        msg = input('Enter message to send: ')
        try:
            s.sendto(msg.encode(), (host, port))
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            print('Server reply: ' + reply.decode())
        except:
            print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
