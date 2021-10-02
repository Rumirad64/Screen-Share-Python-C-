import socket
import random
import json
from time import time
import pyautogui
import base64

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 20000
hostname = socket.gethostname()

with open('serverip.txt') as f:
    lines = f.readline()
    host = lines

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

clientID = random.randint(10000, 90000)
clientID = str(clientID)
print("Client ID -> ", clientID)
ClientSocket.send(str.encode(clientID))
ack = Response = ClientSocket.recv(1024)

with open('clientID.txt', 'w') as f:
    f.write(str(clientID))


tosend = {
    "ClientID": "John",
    "Data": ""

}


while True:
    #Input = input('Say Something: ')

    Response = ClientSocket.recv(1024)
    #ClientSocket.send(str.encode(hostname + " -> " + Input ))
    screenshot = pyautogui.screenshot("Capture.PNG")
    
    print(Response.decode('utf-8'))
    filetosend = open("Capture.PNG", "rb")
    data = filetosend.read()
    
    print("Sending... len -> " , len(data))
    ClientSocket.sendall(data)
    
    filetosend.close()
    
    
    print("Done Sending.")
    print(ClientSocket.recv(1024))
    
    
    """ 
    image = open("Capture.PNG", 'rb')
    image_read = image.read()
    image_64_encode = base64.encodebytes(image_read)
    image_64_encode = image_64_encode.decode("utf-8")

    tosend["Data"] = str(image_64_encode)
    #tosend["Data"] = "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    print(Response.decode('utf-8'))
    ClientSocket.send(str.encode(json.dumps(tosend))) """


ClientSocket.close()
