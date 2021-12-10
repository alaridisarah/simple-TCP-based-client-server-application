import socket
def encodeMessage ( message ): #encryption function
    newMessage=''
    for i in range(len(message)):
        if message[i] != ' ':
            n = ord(message[i]) + 2 #encryption key is +2 of ascicode
            n = chr(n)
            newMessage = newMessage + n
        else:
            newMessage = newMessage + ' '
    return newMessage #encrypted meesage

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket (Ipv4,TCP)
ServerAdress = ('localhost', 21265) #create server (hostAddress, port)
print('Server runing on ', ServerAdress)
Server.bind(ServerAdress) # associate the socket with server
Server.listen(1) # a readiness to accept client connection requests , and number of connection that will accept , if fulll wil rejected
print('Waiting for connection')
connection, ClientAdress = Server.accept() # waits for an incoming connection , if client connect(), return hostaddress,port to client
print('Connection estabilsh ', ClientAdress)
print()
while True : # will recive until client tell stop
    data = connection.recv(1024).decode() # recive form client sendall() at most 1024byte and decode byte to string
    if data : # if data not empty
        if data[0]=='2': # secure mode
            print('Recived: ', data[1:]) #from recv()
            data = encodeMessage(data[1:]) # encode data from encodeMessage()
            print('Send: ',data)
            connection.sendall(data.encode()) # encode string to byte
        elif data[0]=='0': # client quit the appliction
            break
        else : # open mode
            print('Recived: ', data[1:])
            print('Send: ',data[1:])
            connection.sendall(data[1:].encode())
        print()
    else : # empty data , client not send anything
        break


print('Close connection')
connection.close() # connection with client close
Server.close() # socket close


# reference by : https://www.youtube.com/watch?v=6DtinPYTZBY
            #    https://www.youtube.com/watch?v=jgaQAIP4toU
