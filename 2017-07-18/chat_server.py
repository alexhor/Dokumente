import simple_socket, threading

clients = []
client_mutex = threading.Lock()

def waiter_runnable(server_socket):
    while True:
        client = server_socket.accept()
        client_mutex.acquire()
        clients.append(client)
        client_mutex.release()
        new_thread = threading.Thread(target=sender_runnable, args=(client,))
        new_thread.start()


def sender_runnable(client):
    while True:
        message = client.receive()
        if message:
            print("\n" + message)
            client_mutex.acquire()
            for c in clients:
                if c != client:
                    if not c.send(message):
                        try:
                            clients.remove(c)
                        except:
                            pass
            client_mutex.release()
        else:
            client_mutex.acquire()
            try:
                clients.remove(client)
            except:
                pass
            client_mutex.release()
            break


def main():
    print("------ Chat-Server ------\n\nServer-Adresse: ", end='')
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

    server_socket = simple_socket.wait_as_server(server_address, server_port)

    if not server_socket:
        print("\nPort bereits verwendet...")
        return
    
    waiter_thread = threading.Thread(target=waiter_runnable, args=(server_socket,))
    waiter_thread.start()
        

main()
