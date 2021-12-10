import socket
import sys

def decodeMessage ( message ):  #decryption function
    newMessage=''
    for i in range(len(message)):
        if message[i]!=' ':
            n=ord(message[i])-2  #decryption key
            n=chr(n)
            newMessage = newMessage + n
        else :
            newMessage = newMessage + ' '
    return newMessage #decrypted meesage

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket (Ipv4,TCP)
ServerAdress = ('localhost', 21265) # our server address
print('Connecting by ', ServerAdress)
try: # if a server is running
    Client.connect(ServerAdress)
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
    sys.exit() # quit application
Menu = input('''Hi, Which mode you want?
    1) Open Mode
    2) Secure Mode
    3) Quit Application
    \n''')
if Menu=='2':
    print('*Secure Mode Activate*')
elif Menu=='1':
    print('*Open Mode Activate*')
else:
    print('*Quit Appliction*')
while Menu == '1' or Menu=='2': # any of which user choose
    if Menu== '1'  : # open mode
        Message = input('Clinet> ')
        Message = Menu + Message # menu varible will tell the server which mode user choose
        print('Sending: ', Message[1:])
        Client.sendall(Message.encode()) # send for server and will recive in recv
        data=Client.recv(1024).decode() # as echo system client recive from server
        print('Recieved: ', data)
        print('Echo: ',data)
    elif Menu=='2' : #sceure mode
        Message = input('Clinet> ')
        Message = Menu + Message # menu varible will tell the server which mode user choose
        print('Sending: ', Message[1:])
        Client.sendall(Message.encode())# send for server and will recive in recv
        data = Client.recv(1024).decode()# as echo system client recive from server
        print('Recieved: ', data)
        print('ECHO: ', decodeMessage(data)) # here will decode the message that came from client
    exit= input('Finish? [y/n] > ') # ask user if want quit the application
    if exit == 'y': # if y = yes will send to server 0 to tell he want a quit the application
        Client.sendall('0'.encode())
        break

Client.close() # close client socket





