


def depart():
    auTourDe = "le joueur O"
    grille = [["X","X","X","X","X"],
              ["X"," "," "," ","X"],
              [" "," "," "," "," "],
              ["O"," "," "," ","O"],
              ["O","O","O","O","O"]]
    


def millieu():
    auTourDe = "le joueur O"
    grille = [[" ","X","O","X","X"],
              [" "," "," ","O","X"],
              ["X"," "," "," "," "],
              ["O"," ","X"," ","X"],
              ["O","O","O"," ","O"]]


def fin():
    return ...


def main():
    auTourDe = "le joueur O"
    grille = [[" "," ","X","O","X"],
              ["X"," ","O"," ","O"],
              [" "," ","O","O","X"],
              [" ","O","X"," "," "],
              ["X"," "," ","O","X"]]


    print("qu'elle situation de jeu voulais vous:")
    print("                             1/depart")
    print("                             2/le milieu")
    print("                             3/la fin")
    choix = input("saisier un numero: ")
    match choix:
        case 1:
            depart()
        case 2:
            millieu()
        case 3:
            fin()

    


main()