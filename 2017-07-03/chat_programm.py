import json, rotation_encryption, simple_socket, sys, threading, time

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



class ChatProgram:

    def __init__(self):
        self.__running = False
        self.__nickname = None
        self.__my_socket = None
        self.__user_input_thread = None
        self.__socket_input_thread = None

    def launch(self):
        print("------ Chat-Programm ------\n\nServer-Adresse: ", end='')
        server_address = input()
        while True:
            try:
                print("Server-Port: ", end='')
                server_port = int(input())
                if server_port >= 0 and server_port <= 65535:
                    break
                else:
                    print("Ungültige Eingabe!")
            except:
                print("Ungültige Eingabe!")

        print("\nNickname: ", end='')

        self.__nickname = input()

        print("\nVerbinde...")
        
        self.__my_socket = simple_socket.connect_as_client(server_address, server_port)

        if not self.__my_socket:
            print("\nVerbindungsaufbau fehlgeschlagen...")
            return
        
        self.__my_socket.send(self.create_packet_2(self.__nickname, "login"))
        
        self.__user_input_thread = threading.Thread(target=self.user_input_runnable, args=())
        self.__socket_input_thread = threading.Thread(target=self.socket_input_runnable, args=())

        print("\nEingeloggt!\n")

        self.__running = True
        
        self.__user_input_thread.start()
        self.__socket_input_thread.start()


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


    def user_input_runnable(self):
        while self.__running:
            for line in sys.stdin:
                line = line[:len(line) - 1]
                if line == "\\end":
                    json_string = self.create_packet_2(self.__nickname, "logout")
                    self.__my_socket.send(json_string)
                    self.__my_socket.close()
                    print("\nAusgeloggt!\n")
                    self.__running = False
                else:
                    json_string = self.create_packet_1(self.__nickname, line)
                    if not self.__my_socket.send(json_string):
                        self.__running = False
            

    def socket_input_runnable(self):
        while self.__running:
            json_string = self.__my_socket.receive()
            if json_string:
                packet = Packet(json_string)
                if packet.nachrichten_id == 1:
                    print(packet.sender_name + ": " + packet.text)
                elif packet.nachrichten_id == 2:
                    if packet.aktion == "login":
                        print(packet.sender_name + " hat den Chatraum betreten!")
                    elif packet.aktion == "logout":
                        print(packet.sender_name + " hat den Chatraum verlassen!")
            else:
                self.__running = False
                


chat_program = ChatProgram()
chat_program.launch()
