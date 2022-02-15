from flask import Flask, request, Response

server = Flask(__name__)
bag = {}


@server.route('/')
def home():
    global bag

    return "\n".join([f"{k}\t{bag[k]}" for k in bag.keys()])


@server.route('/<key>', methods=['GET'])
def get_data(key):
    global bag

    return bag[key] if key in bag else f'Not found', 200 if key in bag else 404


@server.route('/<key>', methods=['POST'])
def set_data(key):
    global bag

    bag[key] = request.get_data(False, True)
    return bag[key]


@server.route('/is_valid', methods=['POST'])
def is_valid_case():
    global bag

    case = request.get_data(False, True)
    if isinstance(case,int):
        if(not(-1<case<9)):
            return 1
        x=case%3
        y=int((case-x)/3)
        if(bag["grille"][y][x]==' '):
            return 0
    return 1

# give number to player
@server.route('/player_number', methods=['GET'])
def get_player_number():
    global bag
    bag["player_number"] += bag["player_number"]

    return bag["player_number"],200


if __name__ == '__main__':
    nada=" "
    bag["grille"] = [[nada,nada,nada],[nada,nada,nada],[nada,nada,nada]] # contient la grille de case
    bag["player_number"] = 0 # numéro du joueur, incrémenté de 1 à chaque nouveau joueur connecté
    bag["player_turn"] = 1 # numéro joueur qui doit jouer le prochain coup
    bag["status"] = "" # statut de la partie ""="En cours" | "1"="Victoire du joueur 1" | "2"="Victoire du joueur 2" | "3"="Tie"

    server.run()


# à appeler à chaque modification de la grille (reception d'un POST valide d'un joueur)
def check(m):
    #on verifie les colonnes
    for i in range(0,3):
        if(m[i][0]==m[i][1]==m[i][2]!=" "):
            return m[i][0]

    #on verifie les lignes
    for i in range(0,3):
        if(m[0][i]==m[1][i]==m[2][i]!=" "):
            return m[0][i]

    #on verifie les diagonales
    if(m[0][0]==m[1][1]==m[2][2]!=" "):
        return m[1][1]

    if(m[0][2]==m[1][1]==m[2][0]!=" "):
        return m[1][1]

    #on verifie qu'il reste des cases a remplir
    for i in range(0,3):
        for j in range(0,3):
            if(m[i][j]==" "):
                return 0
    return 3

# create a render of the grid
# "-----------"
# "|  |   |  |"
# "|  |   |  |"
# "|  |   |  |"
# "-----------"
def draw(m):
    str = "-------------"+"\n"
    for i in range(0,3):
        str += "|"+m[i][0]+"|"+m[i][1]+"|"+m[i][2]+"|"+"\n"
        str += "-------------"
    return str


@server.route('/grid', methods=['GET'])
def show_grid():
    global bag
    return draw(bag["m"]),200


def game():

    nada=" "
    m = [[nada,nada,nada],[nada,nada,nada],[nada,nada,nada]]
    draw(m)
    j='x'
    while(check(m)):
        # Entrée du joueur
        case=int(input("Entrer un numéro de case entre 1 et 9:"))-1

        if(not(-1<case<9)):
            continue
        x=case%3
        y=int((case-x)/3)
        if(bag["grille"][y][x]==' '):
            bag["grille"][y][x]=j
            j='0' if j=='x' else 'x'
        draw(m)
        #print(x,y)