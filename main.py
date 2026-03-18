


def depart(gille):
    return ...


def millieu(grille):
    return ...


def fin(grille):
    return ...


def main():
    grille = [["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],
              ["","","","","","","","","",""],]


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