# Modul simple_socket v2
#
# Autor: Robin Grether

# Wrapper-Klasse zum Senden und Empfangen von Zeichenketten über einen einfachen socket
class SimpleSocket:

    # Konstruktor
    #
    # my_socket: das socket Objekt
    def __init__(self, my_socket):
        self.my_socket = my_socket
        self.valid = True

    # Empfange eine Nachricht
    #
    # return: Nachricht
    #         oder False, wenn ein Fehler auftrat oder die Zeit abgelaufen ist
    def receive(self, timeout=None):
        if not self.valid:
            return False
        try:
            self.my_socket.settimeout(timeout)
            length = int.from_bytes(self.my_socket.recv(4), byteorder="big", signed=False)
            message = self.my_socket.recv(length).decode("utf-8")
            return message
        except:
            return False

    # Sende eine Nachricht
    #
    # message: Nachricht
    # return: True, wenn die Nachricht erfolgreich gesendet wurde;
    #         ansonsten False
    def send(self, message, timeout=None):
        if not self.valid:
            return False
        try:
            self.my_socket.settimeout(timeout)
            data = message.encode("utf-8")
            self.my_socket.send(len(data).to_bytes(4, byteorder="big", signed=False))
            self.my_socket.send(data)
            return True
        except:
            return False

    # Beende die Verbindung
    #
    # return: True, wenn die Verbindung erfolgreich beendet wurde;
    #         ansonsten False
    def close(self):
        if not self.valid:
            return False
        self.valid = False
        try:
            self.my_socket.shutdown()
            self.my_socket.close()
            return True
        except:
            return False
    


# Binde einen socket an die gegebene Adresse und warte auf genau eine Verbindung
#
# return: socket (SimpleSocket)
#         oder False, falls ein Fehler auftrat oder die Zeit abgelaufen ist
def connect_as_server(server_address="127.0.0.1", server_port=8888, timeout=None):
    try:
        import socket
        server_socket = socket.socket()
        server_socket.settimeout(timeout)
        server_socket.bind((server_address, server_port))
        server_socket.listen(1)
        my_socket = server_socket.accept()[0]
        server_socket.close()
        
        return SimpleSocket(my_socket)
    except:
        return False



# Verbinde zu einem socket unter der gegebenen Adresse
#
# return: socket (SimpleSocket)
#         oder False, falls ein Fehler auftrat oder die Zeit abgelaufen ist
def connect_as_client(server_address="127.0.0.1", server_port=8888, timeout=None):
    try:
        import socket
        my_socket = socket.socket()
        my_socket.settimeout(timeout)
        my_socket.connect((server_address, server_port))

        return SimpleSocket(my_socket)
    except:
        return False



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
    
    if socket:    
        socket.send("Hallo Welt!")
        print(socket.receive())
        socket.close()



#if __name__ == "__main__":
    #run_example()
