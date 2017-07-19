import json, rotation_encryption, simple_socket, sys, threading, time
from PyQt4.QtGui import *

class Packet:

    def __init__(self, json_string=""):
        if json_string == "":
            return
        dictionary = json.loads(json_string)
        if "nachrichten_id" in dictionary:
            self.nachrichten_id = dictionary["nachrichten_id"]
            if self.nachrichten_id == 1:
                encryption_key = dictionary["verschlüsselung"]["parameter"][0]
                if "text" in dictionary["verschlüsselung"]["verschlüsselte_parameter"]:
                    self.text = rotation_encryption.decrypt(dictionary["text"], encryption_key)
                else:
                    self.text = dictionary["text"]
                if "sender_name" in dictionary["verschlüsselung"]["verschlüsselte_parameter"]:
                    self.sender_name = rotation_encryption.decrypt(dictionary["sender_name"], encryption_key)
                else:
                    self.sender_name = dictionary["sender_name"]
            elif self.nachrichten_id == 2:
                self.aktion = dictionary["aktion"]
                self.sender_name = dictionary["sender_name"]
        
    def to_json_string(self):
        if self.nachrichten_id == 1:
            dictionary = {
                "nachrichten_id": self.nachrichten_id,
                "text": rotation_encryption.encrypt(self.text, self.encryption_key),
                "text_länge": len(self.text),
                "verschlüsselung":
                {
                    "algorithmus": "caesar",
                    "parameter": [self.encryption_key],
                    "verschlüsselte_parameter": ["text", "sender_name"]
                },
                "sender_name": rotation_encryption.encrypt(self.sender_name, self.encryption_key),
                "zeitstempel": time.time(),
                "protokoll_version": "0.2"
            }
            return json.dumps(dictionary)
        if self.nachrichten_id == 2:
            dictionary = {
                "nachrichten_id": self.nachrichten_id,
                "aktion": self.aktion,
                "sender_name": self.sender_name,
                "zeitstempel": time.time(),
                "protokoll_version": "0.2"
            }
            return json.dumps(dictionary)

    

#packet = Packet()
#packet.nachrichten_id = 2
#packet.sender_name = "test"
#packet.aktion = "login"
#string = packet.to_json_string()
#
#packet2 = Packet(string)
#if packet2.nachrichten_id == 1:
#    print(packet2.sender_name + ": " + packet2.text)
#elif packet2.nachrichten_id == 2:
#    print(packet2.sender_name + (" hat sich ausgeloggt" if packet2.aktion == "logout" else " hat sich eingeloggt"))


class ChatProgram(QWidget):

    def __init__(self):
        super().__init__()
        self.__running = False
        self.__nickname = None
        self.__my_socket = None
        self.__user_input_thread = None
        self.__socket_input_thread = None


    def init_launch_ui(self):
        self.setWindowTitle("Launch Chat")

        v_box = QVBoxLayout()
        self.setLayout(v_box)

        self.label1 = QLabel("Server-Adresse: ")
        self.line1 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label1)
        h_box.addWidget(self.line1)
        v_box.addLayout(h_box)

        self.label2 = QLabel("Server-Port: ")
        self.line2 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label2)
        h_box.addWidget(self.line2)
        v_box.addLayout(h_box)
        
        self.label3 = QLabel("Username: ")
        self.line3 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label3)
        h_box.addWidget(self.line3)
        v_box.addLayout(h_box)

        self.button_login = QPushButton("Verbinden")
        self.button_login.clicked.connect(self.connect)
        v_box.addWidget(self.button_login)

        self.show()
        

    def connect(self):
        server_address = self.line1.text()
        server_port = self.line2.text()

        try:
            server_port = int(str(server_port))
        except:
            return

        self.__my_socket = simple_socket.connect_as_client(server_address, server_port)

        if not self.__my_socket:
            return

        self.__nickname = self.line3.text()

        self.__my_socket.send(self.create_packet_2(self.__nickname, "login"))
        
        self.__socket_input_thread = threading.Thread(target=self.socket_input_runnable, args=())

        self.init_chat_ui()

        self.__running = True

        self.__socket_input_thread.start()


    def init_chat_ui(self):

        while self.layout().count():
            child = self.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.setWindowTitle("Chat")

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.line = QLineEdit()
        self.line.returnPressed.connect(self.button_clicked)

        self.button = QPushButton("Senden")
        self.button.clicked.connect(self.button_clicked)

        h_box = QHBoxLayout()
        h_box.addWidget(self.line)
        h_box.addWidget(self.button)

        v_box = self.layout()
        v_box.addWidget(self.chat)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

    
    def create_packet_1(self, sender, message):
        packet = Packet()
        packet.nachrichten_id = 1
        packet.sender_name = str(sender)
        packet.text = str(message)
        packet.encryption_key = len(packet.text) % 26
        return packet.to_json_string()

    
    def create_packet_2(self, sender, action):
        packet = Packet()
        packet.nachrichten_id = 2
        packet.sender_name = str(sender)
        packet.aktion = str(action)
        return packet.to_json_string()


    def button_clicked(self):
        line = self.line.text()
        if line == "\\end":
            json_string = self.create_packet_2(self.__nickname, "logout")
            self.__my_socket.send(json_string)
            self.__my_socket.close()
            self.chat.append("\nAusgeloggt!\n")
            self.__running = False
        else:
            self.chat.append(self.__nickname + ": " + line)
            json_string = self.create_packet_1(self.__nickname, line)
            if not self.__my_socket.send(json_string):
                self.__running = False
        self.line.setText("")
            

    def socket_input_runnable(self):
        while self.__running:
            json_string = self.__my_socket.receive()
            if json_string:
                packet = Packet(json_string)
                if packet.nachrichten_id == 1:
                    self.chat.append(packet.sender_name + ": " + packet.text)
                elif packet.nachrichten_id == 2:
                    if packet.aktion == "login":
                        self.chat.append(packet.sender_name + " hat den Chatraum betreten!")
                    elif packet.aktion == "logout":
                        self.chat.append(packet.sender_name + " hat den Chatraum verlassen!")
            else:
                self.__running = False
                


app = QApplication(sys.argv)
chat_program = ChatProgram()
chat_program.init_launch_ui()
sys.exit(app.exec_())
