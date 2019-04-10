# socket_echo_server.py
import socket
import sys
import telepot


# Send message (msg) to users in the list (ids)
def send_tlg_msg(msg, ids):
    x = 1
    bot = telepot.Bot('889358784:AAG6bgRh0lPY6zncZPsH4xcB689rJCJMeeU')
    for id in ids:
       try:
            bot.sendMessage(str(id), str(msg))
       except:
           pass



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 6666)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
send_tlg_msg("Я начал работу", ["@buyqawlogger"])

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(5000)
            print(data.decode('utf-8'))
            send_tlg_msg(data.decode("utf-8"), ["@buyqawlogger"])
            if data:
                print('sending data back to the client')
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

