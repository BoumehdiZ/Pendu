#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ZBoum
#
# Created:     16/04/2020
# Copyright:   (c) ZBoum 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import donnees
import fonctions
import random

def main():

    nom_fichier = donnees.nom_fichier

    nom = input("Saisissez votre nom : ")

    scores = fonctions.scoreLire(nom_fichier)

    liste_lettre = []

    if nom not in scores.keys():
        scores[nom] = 0
        print(scores[nom])

    continue_partie = 'o'

    while(continue_partie != 'n'):
        mot = donnees.liste_mots[(random.randrange(0,len(donnees.liste_mots)))]
        listeOrdi = list(mot.strip())

        motCode = len(mot)* '*'

        vie = donnees.nb_vie

        while(vie > 0):
            print('nombre d\'essaie restant :',vie)
            print(motCode)

            lettre = input('Saisissez une lettre : ')
            lettre = lettre.lower()

            lettre = fonctions.lettreValide(liste_lettre,lettre)
            liste_lettre.append(lettre)

            tupleLettre = fonctions.motValide(listeOrdi, motCode , lettre)
            motCode = tupleLettre[0]
            valide = tupleLettre[1]

            if(valide == False):
                vie = vie - 1

            if(motCode == mot):
                print('nombre d\'essaie restant :',vie)
                print(motCode)
                scores[nom] += vie
                print('Vous avez gagné, le mot était {0} et vôtre score est de {1} points !'.format(mot,scores[nom]))
                break

            if(motCode != mot and vie == 0):
                print("Vous avez perdu !")

        continue_partie = input('Voulez-vous continuer la partie (O/N)?')
        continue_partie = continue_partie.lower()

    fonctions.scoreEcrire(scores,nom_fichier)

if __name__ == '__main__':
    main()
