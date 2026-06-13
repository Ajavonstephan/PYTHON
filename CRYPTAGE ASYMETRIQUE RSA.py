# ============================================
#   RSA - Cryptage Asymétrique en Python
# ============================================
# Menu :
# 1 - Générer les clés
# 2 - Crypter un message
# 3 - Décrypter un message
#
# Petit rappel tragiquement nécessaire :
# RSA réel utilise des très grands nombres.
# Ici c'est une version pédagogique.
# Ne protège pas ton empire criminel avec ça.
# ============================================

import random
from math import gcd

# -----------------------------
# Génération de nombres premiers
# -----------------------------
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generer_premier():
    while True:
        nombre = random.randint(100, 300)
        if est_premier(nombre):
            return nombre


# -----------------------------
# Génération des clés RSA
# -----------------------------
def generer_cles():
    p = generer_premier()
    q = generer_premier()

    while q == p:
        q = generer_premier()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choix de e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calcul de d
    d = pow(e, -1, phi)

    return (e, n), (d, n)


# -----------------------------
# Chiffrement
# -----------------------------
def crypter(message, cle_publique):
    e, n = cle_publique

    message_chiffre = [
        pow(ord(caractere), e, n)
        for caractere in message
    ]

    return message_chiffre


# -----------------------------
# Déchiffrement
# -----------------------------
def decrypter(message_chiffre, cle_privee):
    d, n = cle_privee

    message = ''.join(
        chr(pow(nombre, d, n))
        for nombre in message_chiffre
    )

    return message


# -----------------------------
# Programme principal
# -----------------------------
cle_publique = None
cle_privee = None

while True:

    print("\n===== MENU RSA =====")
    print("1 - Générer les clés")
    print("2 - Crypter un message")
    print("3 - Décrypter un message")
    print("4 - Quitter")

    choix = input("Choix : ")

    # -------------------------
    # Génération des clés
    # -------------------------
    if choix == "1":

        cle_publique, cle_privee = generer_cles()

        print("\nClé publique :", cle_publique)
        print("Clé privée :", cle_privee)

    # -------------------------
    # Chiffrement
    # -------------------------
    elif choix == "2":

        if cle_publique is None:
            print("Tu dois d'abord générer les clés.")
            continue

        message = input("Message à crypter : ")

        message_chiffre = crypter(message, cle_publique)

        print("\nMessage chiffré :")
        print(message_chiffre)

    # -------------------------
    # Déchiffrement
    # -------------------------
    elif choix == "3":

        if cle_privee is None:
            print("Tu dois d'abord générer les clés.")
            continue

        texte = input(
            "Entre les nombres chiffrés séparés par des espaces : "
        )

        message_chiffre = list(map(int, texte.split()))

        message = decrypter(message_chiffre, cle_privee)

        print("\nMessage déchiffré :")
        print(message)

    # -------------------------
    # Quitter
    # -------------------------
    elif choix == "4":

        print("Fin du programme.")
        break

    else:
        print("Choix invalide.")