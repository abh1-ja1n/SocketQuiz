import socket
import pickle
import select
import sys


ip = str(sys.argv[1])
port = int(sys.argv[2])

class Player:
	def __init__(self, id):
		self.id = id
		self.isBuzzerPressed = False
		self.whoPressedBuzzer = id
		self.isPlayerReady = False
		self.isGameReady = False

class Network:
	def __init__(self, ip, port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = ip
		self.port = port
		self.addr = (self.server, self.port)
		self.data = self.connect()

	def getData(self):
		return self.data

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))
		except:
			pass

	def sendData(self, data):
		try:
			self.client.send(pickle.dumps(data))
		#return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)

network = Network(ip, port)
player = network.getData()
print("Hey!! Welcome to the Quiz!! You're Player {}\n".format(player.id+1))

while True:
	if player.isPlayerReady==False:
		print("Press any key,then press enter if you are ready to play.\n")
		reply = input()
		if reply:
			player.isPlayerReady = True
			network.sendData(player)
			break
	network.sendData(player)

while player.isGameReady==False:
	try:
		#network.sendData(player)
		player = pickle.loads(network.client.recv(2048))
	except:
		pass

flag = 0
while True:

    # maintains a list of possible input streams
    #network.sendData(player)
    sockets_list = [sys.stdin, network.client]

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == network.client:
            message = socks.recv(2048)
            message = message.decode("utf-8")
            if message == "":
            	flag = 1
            print(message)
        else:
            message = sys.stdin.readline()
            network.client.send(str.encode(message))
            sys.stdout.flush()
    if flag == 1:
    	break
