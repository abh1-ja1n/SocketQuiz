# SOCKET_QUIZ
This is a socket based mutliplayer quiz made using Python3

### Instructions to run
 - Run the file `server.py` using `python3 server.py <your ip address> <any free port number>`
 - Open three more terminals on the same machine or on different machines connected to same Wi-Fi network
 - On each of the three terminals, run `client.py` using `python3 client.py <your ip address> <server port number>`

This quiz is made for three players. The server has a list of about 50 questions, which gets shuffled at the starting of the quiz. Once, all the players get connected and get ready, a question is sent to them. To answer the  question, they have to press the buzzer in 10 seconds. The player who presses the buzzer gets a chance to answer. There is a time limit of 10 seconds for giving the answer, once the buzzer is pressed. If the answer is correct, the players gains 1 point, otherwise, loses 0.5 points. If no one presses the buzzer, it will continue to give the next question, and no points are deducted. The players who scores 5 or more than 5 points, is declared the winner, and the quiz ends.
