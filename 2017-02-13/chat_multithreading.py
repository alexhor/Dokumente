
import sys
import threading
import simple_socket


from lib.clear import clear







def send_thread():


    client = simple_socket.connect_as_client()
    if client:

        running = True
        while running:

            for line in sys.stdin:

                client.send(line)



def display_thread():

    message_list = []
    server = simple_socket.connect_as_server()
    clear()
    if server:
        running = True
        while running:
            new_message = server.receive()
            if new_message is not False:
                new_message = str(new_message).replace("\r", "").replace("\n", "")
                message_list.append(new_message)
                clear()
                for line in message_list:
                    print("You wrote: " + line)


def chat():

    receiving_threat = threading.Thread(target=display_thread, args=())
    receiving_threat.start()
    sending_threat = threading.Thread(target=send_thread, args=())
    sending_threat.start()




chat()
