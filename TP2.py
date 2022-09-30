"""
programme créé par Marcus Majer
Groupe: 403
Jeu de devinette avec chiffre aléatoire
"""
from random import *
chiffre_recherche = randint(0, 10)

boucle_jeu = True
while boucle_jeu:
    question_chiffre = int(input("J'ai choisi un chiffre entre 0 et 10. À vous de le deviner."))
    if question_chiffre > chiffre_recherche:
        print("Incorrecte, le chiffre est plus petit.")
        boucle_jeu = True
    elif question_chiffre < chiffre_recherche:
        print("Incorrecte, le chiffre est plus grand.")
        boucle_jeu = True
    elif question_chiffre == chiffre_recherche:
        question_fin_jeu = str(input("Vous avez bien deviné le chiffre. Voulez vous rejouer?"))
        if question_fin_jeu == "oui":
            boucle_jeu = True
        elif question_fin_jeu == "non":
            boucle_jeu = False
        else:
            boucle_jeu = True

