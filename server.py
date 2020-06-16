import socket
import pickle
import time
import sys
from _thread import *
import random

questions = [("Who among the following has been named as the TIME magazine Person of the Year 2016?\n a) Narendra Modi  b) Donald Trump  c) Vlamidir Putin  d) Mark Zuckerberg","b"),("Which Indian village has recently earned the tag of becoming India’s first digital village in India?\n a) Akrund  b) Akodara  c) Poshina  d) Punsari","b"),("Who among the following has been elected as US ambassador to the United Nations (UN) by US President-elect Donald Trump?\n a) Nikki Haley  b) Kamala Harris  c) Bobby Jindal  d) Ami Bera","a"),("Name the person who has recently replaced Cyrus Mistry as the Chairman of Tata Global Beverages?\n a) Ratan Tata  b) Lalit Modi  c) Harish Bhat  d) None","c"),("What is the newly launched toll-free helpline number for Unique Identification Authority of India?\n a) 2016  b) 1947  c) 2000  d) 2020","b"),("Which crop is sown on the largest area in India?\n a) Rice  b) Wheat  c) Sugarcane  d) Maize","a"),("Eritrea, which became the 182nd member of the United Nations in 1993, is on the continent of\n a) Asia  b) Africa  c) Europe  d) Australia","b"),("Which of the following personalities gave ‘The Laws of Heredity’?\n a) Robert Hook  b) G J Mendel  c) Charles Darwin  d) William Harvey","b"),("Garampani sanctuary is located at\n a) Junagarh  b) Diphu  c) Kohima  d) Gangtok","b"),("Who is known as “The Saint of Gutters”?\n a) Baba Amte  b) Mother Teresa  c) Anna Hazare  d) None","b"),("For which of the following disciplines is Nobel Prize awarded?\n a) Physics and Chemistry  b) Physiology or Medicine  c) Literature, Peace and Economics  d) All","d"),("Grand Central Terminal, Park Avenue, New York is the world’s\n a) Largest Railway Station  b) Highest Railway Station  c) Longest Railway Station  d) None","a"),("Name the person who was also known as Deshbandhu.\n a) S Radhakrishnan  b) G K Gokhale  c) Chittaranjan Das  d) Madan Mohan Malviya","c"),("FFC stands for\n a) Foreign Finance Corporation  b) Film Finance Corporation  c) Federation of Football Council  d) None","b"),("Which of the following national parks is not listed in a UNESCO World Heritage site?\n a) Kaziranga  b) Keolado  c) Sundarbans  d) Kanha","d"),("The capital of Uttarakhand is\n a) Mussoorie  b) Dehradun  c) Nainital  d) None","b"),("Fastest shorthand writer was\n a) G D Bist  b) J R D Tata  c) J M Tagore  d) Khudada Khan","a"),("In which state has the largest area?\n a) Maharashtra  b) MP  c) UP  d) Rajasthan","d"),(" Geet Govind is a famous creation of\n a) Bana Bhatt  b) Kalidas  c) Jayadev  d) Bharat Muni","c"),("Galileo was an Italian astronomer who\n a) developed the telescope  b) discovered four satellites of Jupiter  c) discovered that the movement of pendulum produces a regular time measurement  d) All","d"),("The Maratha and The Kesri were the two main newspapers which were started by the following people?\n a) Lala Lajpat Rai  b) G K Gokhale  c) Bal Gangadhar Tilak  d) Madan Mohan Malviya","c"),("When did the World Trade Organization come into existence?\n a) 1992  b) 1993  c) 1994  d) 1995","d"),("Exposure to sunlight helps a person to improve his health because\n a) the infrared light kills bacteria in the body  b) resistance power increases  c) the pigment cells in the skin get stimulated and produce a healthy tan  d) the ultraviolet rays convert skin oil into Vitamin D","d"),("The Lucknow session of Indian National Congress that took place in 1916 was presided by\n a) Rashbihari Ghosh  b) Ambika Charan Majumdar  c) Bhupendra Nath Bose  d) None","b"),("In which year did the Cabinet Mission arrived in India?\n a) 1942  b) 1943  c) 1945  d) 1946","d"),("Golf player Vijay Singh belongs to which country?\n a) USA  b) Fiji  c) India  d) UK","b"),("The popular Kumaoni folk singer “Pappu Karki” has passed away. He was releted to which state?\n a) Jammu Kashmir  b) Himanchal Pradesh  c) Uttarakhand  d) Assam","d"),("Panchayat Raj belongs to\n a) Residual List  b) Concurrent List  c) State List  d) Union List","c"),("When did the first Afghan war happen?\n a) 1839  b) 1843  c) 1833  d) 1848","a"),("Which state has the largest population?\n a) UP  b) MP  c) Bihar  d) Maharashtra","a"),("Whose creations are Harshcharita and KadamBari?\n a) Kalhan  b) Panini  c) Bana Bhatta  d) Patanjali","c"),("Gulf cooperation council was originally formed by\n a) Bahrain, Kuwait, Oman, Qatar, Saudi Arabia and United Arab Emirates  b) Second Worls Nations  c) Third World Nations  d) Fourth World Nations","a"),("When the India launched Targeted Public Distribution System?\n a) 1995  b) 1996  c) 1997  d) 1998","c"),("When was the war of american independence?\n a) 1770  b) 1772  c) 1774  d) 1776","d"),("For Olympic and World tournaments, the basketball court has dimensions\n a) 26m x 14m  b) 28m x 15m  c) 27m x 16m  d) 28m x 16m","b"),("In which city the India’s first-ever national police museum will be established?\n a) Chennai  b) Delhi  c) Nagpur  d) Kolkata","b"),("Panini was\n a) a Greek philosopher  b) an Indian astronomer and famous mathematician  c) a Sanskrit grammarian of Vedic times  d) great poet of ancient times","c"),("The winners of which game are honored: Federation Cup, World Cup, Alvin International Trophy and Challenge Cup?\n a) Tennis  b) Volleyball  c) Basketball  d) Cricket","b"),("Under which of the following trees, Buddha got enlightment?\n a) Ficus benghalensis  b) Ficus religiosa  c) Ficus microcarpa  d) Ficus elastica","b"),("Which of the following is the world’s largest and deepest ocean?\n a) Arctic  b) Atlantic  c) Pacific  d) Indian","c"),("World Red Cross and Red Crescent Day are celebrated every year\n a) May 8  b) May 18  c) June 8  d) June 18","a"),(" National emergency arising out of war, armed rebellion or external aggression, belongs to which of the following articles?\n a) Article 280  b) Article 352  c) Article 356 d) Article 370","b"),("The literacy rate of India is\n a) 57.86%  b) 61.34%  c) 63.98%  d) 65.38%","d"),("Famous sculptures depicting the art of love built sometime between 950 and 1050 AD.\n a) Khajuraho Temples  b) Jama Masjid  c) Sun Temple  d) Mahabalipuram Temples","a"),("In which state is the Elephant Falls located?\n a) Mizoram  b) Orissa  c) Manipur  d) Meghalaya","d"),("Which Indian state has the least literacy rate?\n a) Bihar  b) Rajasthan  c) UP  d) Orissa","a"),("Are the Gravity Setting Chambers used in industries for removal?\n a) SOx  b) NOx  c) Suspended Particulate Matter  d) CO","c"),("Which of the following instruments is used to measure Soil Water Tension?\n a) Photometer  b) Pyrometer  c) Psychrometer  d) Tensiometer","d"),("When was SAARC formed?\n a) 1982  b) 1984  c) 1985  d) 1986","c"),("Is the judiciary of the Guwahati High Court?\n a) Nagaland  b) Arunanchal Pradesh  c) Assam  d) All","d")]
random.shuffle(questions)

boolean = [False, False, False]

whoPressedBuzz = -1

list_of_clients = []

score = [0,0,0]

helper1 = 0
helper2 = 0

class Player():
	def __init__(self, id):
		self.score = 0
		self.id = id
		self.isBuzzerPressed = False
		self.whoPressedBuzzer = id
		self.isPlayerReady = False
		self.isGameReady = False


server = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	print(e)

s.listen(100)
print("Waiting for a connection, Server Started")

players = [Player(0), Player(1), Player(2)]

def client_thread(conn, curr_player):
	#conn.send("Hey!! Welcome to the Quiz")
	conn.send(pickle.dumps(players[curr_player]))

	MakeAllReady(conn)

	reply = ""

	Quiz(conn, players[curr_player].id)
	conn.close()
	sys.exit()


def MakeAllReady(conn):
	while True:
		try:
			player = pickle.loads(conn.recv(2048))
			if player.isPlayerReady:
				boolean[player.id] = True
				print("Player {} is ready".format(player.id+1))
				conn.send(pickle.dumps(player))
				break
		except:
			pass
	while True:
		try:
			if boolean == [True, True, True]:
				player.isGameReady = True
				print("ALL READY")
				conn.send(pickle.dumps(player))
				break
			conn.send(pickle.dumps(player))
		except:
			pass


def Quiz(conn, player_id):
	global score
	for question in questions:
		if score[0] < 5 and score[1] < 5 and score[2] < 5:
			global whoPressedBuzz
			#player = pickle.loads(conn.recv(2048))
			time.sleep(1)
			print("Sending next question to Player {}, whose answer is option {}.\n".format(player_id+1, question[1]))
			conn.send(str.encode(question[0]+"\n"))
			start_time = time.time()
			conn.send(str.encode("Press Buzzer(Enter key) to give the answer in 10 seconds.\n"))
			helper3 = 0
			while(time.time()-start_time<=10):
				conn.settimeout(0.5)
				#print("{} seconds left".format(time.time()-start_time))
				try:
					data = conn.recv(2048)
					data = data.decode("utf-8")
				except:
					data = None
				if data and whoPressedBuzz == -1:
					whoPressedBuzz = player_id + 1
					conn.send(str.encode("Now, you have 10 seconds to enter the right option among a, b, c and d.\n"))
					helper3 = 1
					break
				if whoPressedBuzz != player_id + 1 and whoPressedBuzz != -1:
					conn.send(str.encode("Player {} has pressed the buzzer. Wait for him/her to answer.\n".format(whoPressedBuzz)))
					helper3 = 1
					break
			answer_time = time.time()
			global helper1
			global helper2
			myhelper = 0
			if helper3==0:
				conn.send(str.encode("Time limit to press the buzzer exceeded.\n The right option is option {}\n".format(question[1])))
			while(time.time()-answer_time<=10 and helper3==1):
				if whoPressedBuzz == player_id + 1:
					conn.settimeout(10)
					try:
						answer = conn.recv(2048)
						answer = answer.decode("utf-8")
						if answer == question[1] + "\n":
							score[player_id] += 1
							whoPressedBuzz = -1
							myhelper = 1
							helper1 = 1
							helper2 = 1
							conn.send(str.encode("Correct answer!! You got 1 point.\n"))
						else:
							score[player_id] -= 0.5
							helper1 = 1
							myhelper = 1
							helper2 = 1
							whoPressedBuzz = -1
							conn.send(str.encode("Ahh!! Wrong answer!! You lose half point.\n"))
					except:
						score[player_id] -= 0.5
						whoPressedBuzz = -1
						helper1 = 1
						helper2 = 1
						conn.send(str.encode("Time limit exceeded. You lose half point.\n"))
				if helper1 == 1:
					helper1 = 0
					whoPressedBuzz = -1
					break
				if helper2 == 1 and helper1 == 0:
					helper2 = 0
					whoPressedBuzz = -1
					break
				if myhelper == 1:
					break
			conn.send(str.encode("Scores:- \n"))
			conn.send(str.encode("         Player 1 : {} points\n".format(score[0])))
			conn.send(str.encode("         Player 2 : {} points\n".format(score[1])))
			conn.send(str.encode("         Player 3 : {} points\n".format(score[2])))
		else:
			break
	
	if score[player_id] >= 5:
		print("Player {} WON\n".format(player_id+1))
		conn.send(str.encode("YOU WON"))
	else:
		if score[0]>=5 and player_id!=0:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(1)))
		if score[1]>=5 and player_id!=1:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(2)))
		if score[2]>=5 and player_id!=2:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(3)))



curr_player = 0
while score[0]<5 and score[1]<5 and score[2]<5:
	s.settimeout(1)
	try:
		conn, addr = s.accept()
		list_of_clients.append(conn)
		print("Connected to:", addr)
	except:
		if score[0]>=5 or score[1]>=5 or score[2]>=5:
			print("Quiz finished")
		continue

	start_new_thread(client_thread, (conn, curr_player))
	curr_player += 1

s.close()

