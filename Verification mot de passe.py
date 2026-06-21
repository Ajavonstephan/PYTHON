import string

password = input("Entre un mot de passe à tester : ")

# On va verifier la longueur
if len(password) < 8:
    niveau = "faible"
else:
    score = 0
    # On va verifier s'il contient un mot de passe
    if any(c.isupper() for c in password): score += 1

    # On va verifier s'il contient un chiffre
    if any(c.isdigit() for c in password): score += 1
    
    # On va verifier s'il contient un caractere special
    if any(c in string.punctuation for c in password): score += 1

    if score <= 1:
        niveau = "faible"
    elif score == 2:
        niveau = "moyen"
    else:
        niveau = "fort"

print("Mot de passe", niveau)