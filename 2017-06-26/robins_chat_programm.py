import json, rotation_encryption, simple_socket, sys, threading, time

def create_packet_1(sender, message):
    sender = str(sender)
    message = str(message)
    message_length = len(message)
    encryption_key = message_length % 26
    sender_encrypted = rotation_encryption.encrypt(sender, encryption_key)
    message_encrypted = rotation_encryption.encrypt(message, encryption_key)
    timestamp = time.time()

    packet = {
                "nachrichten_id": 1,
                "text": message_encrypted,
                "text_länge": message_length,
                "verschlüsselung":
                {
                    "algorithmus": "caesar",
                    "parameter": [encryption_key],
                    "verschlüsselte_parameter": ["text", "sender_name"]
                },
                "sender_name": sender_encrypted,
                "zeitstempel": timestamp,
                "protokoll_version": "0.2"
            }

    packet_json = json.dumps(packet)
    return packet_json

def create_packet_2(sender, action):
    sender = str(sender)
    action = str(action)
    timestamp = time.time()

    packet = {
                "nachrichten_id": 2,
                "aktion": action,
                "sender_name": sender,
                "zeitstempel": timestamp,
                "protokoll_version": "0.2"
            }

    packet_json = json.dumps(packet)
    return packet_json

def packet_from_json(json_string):
    try:
        return json.loads(json_string)
    except:
        return False

def user_input_runnable():
    global my_socket, nickname, running
    while running:
        for line in sys.stdin:
            line = line[:len(line) - 1]
            if line == "\\end":
                json_string = create_packet_2(nickname, "logout")
                my_socket.send(json_string)
                my_socket.close()
                print("\nAusgeloggt!\n")
                running = False
            else:
                json_string = create_packet_1(nickname, line)
                if not my_socket.send(json_string):
                    running = False
            

def socket_input_runnable():
    global my_socket, running
    while running:
        json_string = my_socket.receive()
        if json_string:
            packet = packet_from_json(json_string)
            if packet:
                if packet["nachrichten_id"] == 1:
                    encryption_key = packet["verschlüsselung"]["parameter"][0]
                    message = rotation_encryption.decrypt(packet["text"], encryption_key) if "verschlüsselte_parameter" in packet["verschlüsselung"] and "text" in packet["verschlüsselung"]["verschlüsselte_parameter"] else packet["text"]
                    sender = rotation_encryption.decrypt(packet["sender_name"], encryption_key) if "verschlüsselte_parameter" in packet["verschlüsselung"] and "sender_name" in packet["verschlüsselung"]["verschlüsselte_parameter"] else packet["sender_name"]
                    print(sender + ": " + message)
                elif packet["nachrichten_id"] == 2:
                    action = packet["aktion"]
                    sender = packet["sender_name"]
                    if action == "login":
                        print(sender + " hat den Chatraum betreten!")
                    elif action == "logout":
                        print(sender + " hat den Chatraum verlassen!")
        else:
            running = False
            

running = True
nickname = None
my_socket = None
user_input_thread = None
socket_input_thread = None

def main():
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

    global nickname
    nickname = input()

    print("\nVerbinde...")
    
    global my_socket
    
    my_socket = simple_socket.connect_as_client(server_address, server_port)

    if not my_socket:
        print("\nVerbindungsaufbau fehlgeschlagen...")
        return
    
    my_socket.send(create_packet_2(nickname, "login"))
    
    global user_input_thread
    global socket_input_thread
    
    user_input_thread = threading.Thread(target=user_input_runnable, args=())
    socket_input_thread = threading.Thread(target=socket_input_runnable, args=())

    print("\nEingeloggt!\n")
    
    user_input_thread.start()
    socket_input_thread.start()
    
    
main()
