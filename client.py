import socket
import sys

try:
	UDP_IP_ADDRESS = ""
	if len(sys.argv) <= 1:
		UDP_IP_ADDRESS = input("Specify an IP Address: ")
	else:
		UDP_IP_ADDRESS = sys.argv[1]
	UDP_PORT_NO = 3333
	try:
		socket.inet_aton(UDP_IP_ADDRESS)
	except socket.error:
		print("{} is not a valid IP Address.".format(UDP_IP_ADDRESS))
		quit()

	msg = "h"
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		msg = input("Enter your message: ")
		clientSock.sendto(msg.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
		print("Sending {}...".format(msg))
except:
	print("Script failed to run, are you using Python3?")

