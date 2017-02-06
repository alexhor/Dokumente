# Sockets - Datenaustausch über Netzwerke

# Modul importieren
import simple_socket

# Beispiel ausführen
simple_socket.run_example()

# Programm beenden
import sys
sys.exit()



# ------ jetzt eigener Code (Server) ------

# erzeugt den Socket
my_socket = simple_socket.connect_as_server()

# sende eine Nachricht
my_socket.send("Hallo Client!")

# empfange eine Nachricht
message = my_socket.receive()
print(message)

# beende die Verbindung
my_socket.close()



# ------ jetzt eigener Code (Client) ------

# erzeugt den Socket
my_socket = simple_socket.connect_as_client()

# empfange eine Nachricht
message = my_socket.receive()
print(message)

# sende eine Nachricht
my_socket.send("Hallo zurück!")

# beende die Verbindung
my_socket.close()


