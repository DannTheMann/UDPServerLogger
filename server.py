import socket
import datetime
import os

UDP_IP      = "0.0.0.0"
UDP_PORT    = 3333
FILE_PATH   = "logs/"

def writeToFile(context):
    print("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M] ") + context)
    f = open(FILE_PATH + datetime.datetime.now().strftime("%Y-%m-%d") + ".log", "a")
    f.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M] ") + context + "\n")
    f.close()

def udpServer():
    print("Hosting UDP Server on port: {}".format(UDP_PORT))

    if not os.path.exists(FILE_PATH):
        print("File path '{}' did not exist, creating it.".format(FILE_PATH))
        os.makedirs(FILE_PATH)   

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        msg = "{}: {}".format(addr[0], data)
        writeToFile(msg)

def __main__():
    print("")
    print("")
    print(" ----------- ")
    print("")
    print("")
    print("Starting application. Time: {}".format(datetime.datetime.now()))
    udpServer()

__main__()

