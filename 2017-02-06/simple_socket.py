# Modul simple_socket
#
# Autor: Robin Grether

# Wrapper-Klasse zum Senden und Empfangen von Zeichenketten
# über einen einfachen socket
class SimpleSocket:

    # Konstruktor
    #
    # my_socket: das socket Objekt
    def __init__(self, my_socket):
        self.my_socket = my_socket

    # Empfange eine Nachricht
    #
    # return: Nachricht
    def receive(self):
        length = int.from_bytes(self.my_socket.recv(4), byteorder="big", signed=False)
        return self.my_socket.recv(length).decode("utf-8")

    # Sende eine Nachricht
    #
    # message: Nachricht
    # return: True
    def send(self, message):
        data = message.encode("utf-8")
        self.my_socket.send(len(data).to_bytes(4, byteorder="big", signed=False))
        self.my_socket.send(data)
        return True

    # Beende die Verbindung
    #
    # return: True
    def close(self):
        self.my_socket.close()
        return True
    


# Binde einen socket an die gegebene Adresse und warte auf
# eine Verbindung
#
# return: socket gewrappt als SimpleSocket
def connect_as_server(server_address="127.0.0.1", server_port=8123):
    import socket
    server_socket = socket.socket()
    server_socket.bind((server_address, server_port))
    server_socket.listen(1)
    my_socket = server_socket.accept()[0]
    server_socket.close()

    return SimpleSocket(my_socket)



# Verbinde zu einem socket unter der gegebenen Adresse
#
# return: socket gewrappt als SimpleSocket
def connect_as_client(server_address="127.0.0.1", server_port=8123):
    import socket
    my_socket = socket.socket()
    my_socket.connect((server_address, server_port))

    return SimpleSocket(my_socket)



# Führt ein Beispiel aus
def run_example():
    print("Server (s) oder Client (c) ?")
    choice = input()
    
    if choice == "s":
        socket = connect_as_server()
    elif choice == "c":
        socket = connect_as_client()
    else:
        print("Unbekannte Funktion!")
        return
        
    socket.send("Hallo Welt!")
    print(socket.receive())
    socket.close()



if __name__ == "__main__":
    run_example()
