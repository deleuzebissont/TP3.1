import random

niveau_de_vie = 20
nb_victoires = 0
nb_defaites = 0
nb_combats = 0
numero_adversaire = 1
statut_combat = ""
nb_victoires_consecutives = 0


# je creer une fonction afin d y stocker mon jeu
def mygame():
    # je global mes variables afin de pouvoir les utiliser dans ma fonction
    global nb_combats, numero_adversaire, niveau_de_vie, nb_defaites, nb_victoires, statut_combat
    global nb_victoires_consecutives
    # j execute mon code tant que la vie de l utilisateur n est pas de 0
    while niveau_de_vie > 0:
        # je definis mes deux des puis je les additione
        dee_1 = random.randint(1, 6)
        dee_2 = random.randint(1, 6)
        somme_des_des = dee_1 + dee_2
        # si le personnage gagne 3 fois de suite, il tombe contre un boss
        if nb_victoires_consecutives >= 3:
            force_adversaire = random.randint(10, 15)
        else:
            force_adversaire = random.randint(0, 12)
        print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire}")
        # je donne a l utilisateur ses choix
        choice = input("""
Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
>
""")
        if choice == "1":
            # je donne a l utilisateur des informations sur le combat
            print(f"""
Adversaire : adversaire numero {numero_adversaire}
Force de l’adversaire : {force_adversaire}
Niveau de vie de l’usager : {niveau_de_vie}
Combat {nb_combats} : {nb_victoires} victoires vs {nb_defaites} defaites
""")
            print(f"Premier dée : {dee_1} Deuxieme dée : {dee_2} .Leur somme est donc: {somme_des_des}")
            # si l utilisateur gagne le combat, on ajuste les informations, ex : nb de combats
            if somme_des_des > force_adversaire:
                statut_combat = "Victoire"
                numero_adversaire += 1
                nb_combats += 1
                nb_victoires += 1
                niveau_de_vie += force_adversaire
                print(statut_combat + "!")
                print(f"Vous avez {niveau_de_vie} vies")
                nb_victoires_consecutives += 1
                print(f"Nombre de victoires consecutives : {nb_victoires_consecutives}")
            # si l utilisateur perd le combat, on ajuste egalement les informations ex : nb de defaites
            elif somme_des_des <= force_adversaire:
                statut_combat = "Defaite"
                numero_adversaire += 1
                nb_combats += 1
                nb_defaites += 1
                nb_victoires_consecutives = 0
                niveau_de_vie -= force_adversaire
                print(f"Vous avez {niveau_de_vie} vies")
                print(statut_combat + "!")
                nb_victoires_consecutives = 0
                print(f"Nombre de victoires consecutives : {nb_victoires_consecutives}")
        # si l utilisateur choisis de s enfuir, il perd 1 vie
        elif choice == "2":
            niveau_de_vie -= 1
            print(f"Vous avez perdu 1 vie et vous avez maintenant {niveau_de_vie} vies.")
        # si l utilisateur choisis de voir les regles, on les print
        elif choice == "3":
            print("""
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
  """)
        # si le choix est de quitter, on quitte la loop et on affiche un message d au revoir
        elif choice == "4":
            print("Merci d avoir jouer, au revoir... ")
            break
    print("Vous avez perdu, bien essayé...")

# on execute le contenu de la fonction
mygame()
