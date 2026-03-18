
def afficher_grille(grille):
    print("______________________________")
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if j == len(grille[0])-1:
                print(f"|{grille[i][j]}|")
            else:
                print(f"|{grille[i][j]}", end=" ")





def depart():
    auTourDe = "le joueur O"
    grille = [["X","X","X","X","X"],
              ["X"," "," "," ","X"],
              [" "," "," "," "," "],
              ["O"," "," "," ","O"],
              ["O","O","O","O","O"]]
    afficher_grille(grille)
    


def millieu():
    auTourDe = "le joueur O"
    grille = [[" ","X","O","X","X"],
              [" "," "," ","O","X"],
              ["X"," "," "," "," "],
              ["O"," ","X"," ","X"],
              ["O","O","O"," ","O"]]
    afficher_grille(grille)


def fin():
    auTourDe = "le joueur O"
    grille = [[" "," ","X","O","X"],
              ["X"," ","O"," ","O"],
              [" "," ","O","O","X"],
              [" ","O","X"," "," "],
              ["X"," "," ","O","X"]]
    afficher_grille(grille)
    

def main():

    print("qu'elle situation de jeu voulais vous:")
    print("                             1/depart")
    print("                             2/le milieu")
    print("                             3/la fin")
    choix = input("saisier un numero: ")
    if choix == "1":
        print("1")
        depart()
    elif choix =="2":
        millieu()
    else:
        fin()
    
    


main()