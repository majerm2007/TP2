"""
programme créé par Marcus Majer
Groupe: 403
Jeu de devinette avec chiffre aléatoire
"""
from random import *

boucle_jeu = True


while boucle_jeu:
    chiffre_recherche = randint(0, 10)
    nb_essaie = 1

    not_found = True
    while not_found:
        question_chiffre = int(input("J'ai choisi un chiffre entre 0 et 10. À vous de le deviner."))
        if question_chiffre > chiffre_recherche:
            print("Incorrecte, le chiffre est plus petit.")
            nb_essaie += 1

        elif question_chiffre < chiffre_recherche:
            print("Incorrecte, le chiffre est plus grand.")
            nb_essaie += 1

        elif question_chiffre == chiffre_recherche:
            question_fin_jeu = str(input(f"Vous avez bien deviné le chiffre en {nb_essaie} essaies. Voulez vous rejouer?"))
            if question_fin_jeu == "oui":
                boucle_jeu = True
                not_found = False
            elif question_fin_jeu == "non":
                not_found = False

