"""
programme créé par Marcus Majer
Groupe: 403
Jeu de devinette avec chiffre aléatoire
"""
from random import *

chiffre_recherche = randint(0,10)

boucle_jeu = True
while boucle_jeu:
    question_chiffre = int(input("J'ai choisi un chiffre entre 0 et 10. À vous de le deviner."))
    if question_chiffre > chiffre_recherche:
        print("Incorrecte, le chiffre est plus petit.")
    elif question_chiffre < chiffre_recherche:
        print("Incorrecte, le chiffre est plus grand.")

    boucle_jeu = False



