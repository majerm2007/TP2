"""
programme créé par Marcus Majer
Groupe: 403
Description: Jeu de devinette avec chiffre aléatoire
"""
from random import randint

boucle_jeu = True

def borne_jeu():
    global nb_maximum
    global nb_minimum
    nb_maximum = int(input("Choisissez le chiffre maximale dans lequel vous devinerez le chiffre"))
    nb_minimum = int(input("Choisissez le chiffre minimale dans lequel vous devinerez le chiffre"))

"""
définition de la fonction des bornes du jeu qui assurent le fait que le joueur peut choisir entre quels deux chiffres il devra deviner un chiffre
"""

while boucle_jeu:

    borne_jeu()
    chiffre_recherche = randint(nb_minimum, nb_maximum)
    nb_essaie = 1

    not_found = True
    while not_found:
        question_chiffre = int(input(f"J'ai choisi un chiffre entre {nb_minimum} et {nb_maximum}. À vous de le deviner."))
        if question_chiffre > chiffre_recherche:
            print("Incorrecte, le chiffre est plus petit.")
            nb_essaie += 1

        elif question_chiffre < chiffre_recherche:
            print("Incorrecte, le chiffre est plus grand.")
            nb_essaie += 1

        elif question_chiffre == chiffre_recherche:
            question_fin_jeu = str(input(f"Bravo, bonne réponse! Vous avez bien deviné le chiffre en {nb_essaie} essaies. Voulez vous rejouer? (oui/non)"))
            if question_fin_jeu == "oui":
                boucle_jeu = True
                not_found = False
            elif question_fin_jeu == "non":
                not_found = False
                boucle_jeu = False

