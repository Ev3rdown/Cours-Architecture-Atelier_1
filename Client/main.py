import socket


def request(verb, url, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 5000))
        sock.send(f"{verb} /{url} HTTP/1.1\r\n".encode())
        sock.send("Content-Type: text/plain\r\n".encode())
        sock.send(f"Content-Length: {len(value)}\r\n\r\n".encode())
        sock.send(f"{value}\r\n".encode())
        while True:
            s = sock.recv(4096).decode('utf-8')
            if s == '':
                break;
            print(s)
        sock.close()

def get_player_number():
    request("GET","player_number",)
    # Parser la requête/trouver une autre méthode
    return 1;

if __name__ == '__main__':

    player_number = get_player_number()

    while player_number(1):
        print("Joueur 1 a vous de jouer :")
        player_choice = input(f"Choisissez une case :")
        player_number = player_choice
        else:
            items = content.split('/')
            if len(items) > 1:
                request("POST", items[0], items[1])
                request("GET", "", "")
            else:
                request("GET", items[0],"")



    while True:
        content = input("Joueur X veuillez choisir une case :")
        if content == ("2"):
            request("POST", items[0])
            break
        else:
            items = content.split('/')
            if len(items) > 1:
                request("POST", items[0], items[1])
                request("GET", "", "")
            else:
                request("GET", items[0],"")
