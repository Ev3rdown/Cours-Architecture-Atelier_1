from enum import Enum
import socket
from time import sleep

class Status(Enum):
    GAME = 0
    PLAYER = 0

def request(verb, url, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 5001))
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
    request("GET","player_number","")
    # Parser la requête/trouver une autre méthode
    return 1;

def update_status(status_GAME,status_PLAYER):
    req = request("GET","status","")
    status_GAME = 0;
    status_PLAYER = 1;

if __name__ == '__main__':

    player_number = get_player_number()
    status_GAME=0
    status_PLAYER=1
    update_status(status_GAME,status_PLAYER)

    print("Vous êtes le joueur "+str(player_number))
    while status_GAME==0:
        if status_PLAYER==player_number:
            request("GET","grid","")
            print("Joueur "+ str(player_number) +" a vous de jouer :")
            case=int(input("Entrer un numéro de case entre 1 et 9:"))-1
            req = request("POST","play",str(player_number)+"="+str(case))
            print("sent post")
            if req == 1:
                print("Erreur")
                continue
        else:
            print("En attente de l'autre joueur")
        update_status(status_GAME,status_PLAYER)
        sleep(1)
    if status_GAME!=3:
        print("Victoire du joueur "+str(status_GAME))
    elif status_GAME==3:
        print("Pas de vainqueur")
    else:
        print("Erreur Fatale")