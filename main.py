
 # -*- coding: utf-8 -*-

def afficher_grille(grille,auTourDe):
    print("______________________________")
    if auTourDe:
        print("c'est au joueur au X de jouer\n")
    else: 
        print("c'est au joueur au O de jouer\n")
    print("    1  2  3  4  5")
    convNbLettre ={0:'A',1:'B',2:'C',3:'D',4:'E'}
    for i in range(len(grille)):
        print(convNbLettre[i], end=" ")
        for j in range(len(grille[0])):
            if j == len(grille[0])-1:
                print(f"|{grille[i][j]} |")
            else:
                print(f"|{grille[i][j]}", end=" ")



def demanderUneCase():
    ligne = input("saisissez une ligne: ")
    colonne = input("saisissez une colonne: ")
    




def depart():
    auTourDe = 1 #quand c'est a True c'est au joueur au X et quand c'est a false au joueur au O 
    grille = [["X","X","X","X","X"],
              ["X"," "," "," ","X"],
              [" "," "," "," "," "],
              ["O"," "," "," ","O"],
              ["O","O","O","O","O"]]
    afficher_grille(grille,auTourDe)
    


def millieu():
    auTourDe = 1 #quand c'est a True c'est au joueur au X et quand c'est a false au joueur au O 
    grille = [[" ","X","O","X","X"],
              [" "," "," ","O","X"],
              ["X"," "," "," "," "],
              ["O"," ","X"," ","X"],
              ["O","O","O"," ","O"]]
    afficher_grille(grille,auTourDe)


def fin():
    auTourDe = True #quand c'est a True c'est au joueur au X et quand c'est a false au joueur au O 
    grille = [[" "," ","X","O","X"],
              ["X"," ","O"," ","O"],
              [" "," ","O","O","X"],
              [" ","O","X"," "," "],
              ["X"," "," ","O","X"]]
    afficher_grille(grille,auTourDe)
    

def main():

    print("qu'elle situation de jeu voulais vous:")
    print("                             1/depart")
    print("                             2/le milieu")
    print("                             3/la fin")
    choix = input("saisier un numero: ")
    match choix:
        case "1":
            depart()
        case "2":
            millieu()
        case "3":
            fin()
    
def est_au_bon_format(message):
    ...


def est_dans_grille():
    ...


main()