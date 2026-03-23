# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs
#### REPRESENTATION DES DONNEES
###initialisation des grilles et autres variables de jeu


# grille qui represente la position initiale.
grille_deput = [["X","X","X","X","X"],
              ["X"," "," "," ","X"],
              [" "," "," "," "," "],
              ["O"," "," "," ","O"],
              ["O","O","O","O","O"]]


# grille qui represente une position possible au millieu de la partie.
grille_millieu = [[" ","X","O","X","X"],
                  [" "," "," ","O","X"],
                  ["X"," "," "," "," "],
                  ["O"," ","X"," ","X"],
                  ["O","O","O"," ","O"]]

#grille qui represente une position possible a la fin de la partie.
grille_fin =[[" "," ","X","O","X"],
             ["X"," ","O"," ","O"],
             [" "," ","O","O","X"],
             [" ","O","X"," "," "],
             ["X"," "," ","O","X"]]

#### REPRESENTATION GRAPHIQUE
def afficher_grille(grille:list)->None:
    print("______________________________")
    print("    1  2  3  4  5")
    convNbLettre ={0:'A',1:'B',2:'C',3:'D',4:'E'}
    for i in range(len(grille)):
        print(convNbLettre[i], end=" ")
        for j in range(len(grille[0])):
            if j == len(grille[0])-1:
                print(f"|{grille[i][j]} |")
            else:
                print(f"|{grille[i][j]}", end=" ")

#### SAISIE
###fonctions de verification
#jeux de tests
def test_est_dans_grille():
    assert est_dans_grille("A",1,grille_deput),"dans la grille doit renvoyer True."
    assert not est_dans_grille("1",1,grille_deput),"mauvais format doit revoyer False."
    assert not est_dans_grille("A",7,grille_deput),"ligne dans la grille, mais collone en dehors doit renvoyer False."
    assert not est_dans_grille("T",1,grille_deput),"ligne en dehors de la grille et collene dedans doit renvoyer False."
    assert not est_dans_grille("F",11,grille_deput),"ligne en dehors de la grille et collone en dehors doit renvoyer False."
    


#verification dans grille
def est_dans_grille(ligne:str, colonne:int, grille:list)->bool:
    convNbLettre ={'A':0,'B':1,'C':2,'D':3,'E':4}
    if ligne not in convNbLettre.keys():
        return False
    return len(grille)>convNbLettre[ligne] and len(grille)>colonne-1

###fonctions de saisie
def saisir_coordonnees(grille):
    cherche_coordonnees = True
    while cherche_coordonnees:
        coordonnees = input("choisicer des coordoner: ")
        if len(coordonnees)!=2:
            continue
        elif not est_dans_grille(coordonnees[0],int(coordonnees[1]),grille):
            continue
        else:
            return coordonnees


#### CODE PRINCIPAL
# execution affichage sur les 3 grilles et autres variables de jeux
afficher_grille(grille_deput)
afficher_grille(grille_millieu)
afficher_grille(grille_fin)

#execution test est_dans_grille
test_est_dans_grille() #uniquement pour la mise au point, a conserver pour le correcteur

#affichage des coordonnees saisies
print(f"les coordonnees saisit sont: {saisir_coordonnees(grille_deput)}")
