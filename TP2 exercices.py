# exercice a
print("Hello World!")

# exercice b
nom = input("Quel est ton nom ? : ")
print(f"Bonjour ! {nom}")

# exercice c
nb_etoiles = int(input("Combien d etoiles voulez vous ? : "))
while nb_etoiles != 0:
    print(nb_etoiles * "*")
    nb_etoiles -= 1
