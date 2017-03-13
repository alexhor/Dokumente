import sys, json
from lib import simple_socket
from time import time


def send():
    # endlosschleife
    for line in sys.stdin:
        # verschlüsseln
        # line in json konvertieren
        # daten an den Server senden

def receive():
    # endlosschleife
        # daten empfangen
        # in dictionary konvertieren
        # entschlüsseln
        # ausgeben

def encrypt(user_input, shifting_number):
    return user_input

def decrypt(user_input, shifting_number):
    return user_input

# thread für send()
# thread für receive()


message = {
  "nachrichten_id": 1,
  "text": "Keine Panik!",
  "text_länge": 12,
  "verschlüsselung": 
  {
    "algorithmus": "caesar",
    "parameter": [26]
  },
  "sender_name": "ArthurDent42",
  "zeit_stempel": time(),
  "protokoll_verion": "0.1"
}
