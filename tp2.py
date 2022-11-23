import random

borne_min = 0
borne_max = 100


def borne():
    global borne_min
    global borne_max
    choix_borne = input("Voulez vous choisir vos bornes ? Oui(O) Non(N) :")
    if choix_borne.upper() == "O":
        borne_min = int(input("Quelle est votre borne minimale :"))
        borne_max = int(input("Quelle est votre borne maximale :"))
        if borne_min > borne_max:
            borne_min, borne_max = borne_max, borne_min
        return borne_min, borne_max


borne()
print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}.")
print("À vous de le deviner...")
guess = 0
final_answer = "O"
value = 0


def choose_number():
    global value
    value = random.randint(borne_min, borne_max)
    return value


while final_answer.upper() == "O":
    choose_number()
    guess_count = 0
    while guess != value:
        guess = int(input("Entrez votre essai : "))
        if guess > value:
            print(f"Mauvaise choix, le nombre est plus petit que {guess}")
            guess_count += 1
        elif guess < value:
            print(f"Mauvais réponse, le nombre est plus grand que {guess}")
            guess_count += 1
        else:
            guess_count += 1
            print("Bravo ! Bonne réponse.")
            print(f"Vous avez reussis en : {guess_count} essai(s).")
            final_answer = input("Souhaitez vous faire une nouvelle partie Oui (O) Non (N): ")
            if final_answer.upper() == "O":
                borne()
                print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}.")
                print("À vous de le deviner...")
            else:
                print("Vous avez quittez le jeu.")
