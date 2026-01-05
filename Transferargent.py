Solde = 100000

def Show_Menu():
    print("===== MENU PRINCIPAL=====")
    print("\n1. Transfert d'argent")
    print("2. Retrait d'argent")
    print("3. Solde")
    print("4. Quitter")

while True:
    Show_Menu()
    choixmenu = input("Entrer votre choix:")

    if choixmenu == "1":
       Montant = int(input("Entrer le montant:"))
       Numero = int(input("Entrer le numero:"))
       print("Vous allez envoyer", Montant, "F à", Numero)
       print("1. Annuler")
       print("2. Confirmer")
    
       choixconfirm = input("Entrer votre choix:")

       if choixconfirm == "1":
          print("Merci Aurevoir")
       elif choixconfirm == "2":
           if Solde >= Montant:
              Solde -= Montant
              print("Votre transfert de", Montant, "F à", Numero, "à bien été éffectué.\nVotre nouveau solde est de:",Solde)
           else:
              print("Votre solde est insuffisant pour effectuer ce transfert")
       else:
          print("Choix invalide, veuillez reesayer.")

       Retour = int(input("ENTRER 0 POUR ALLER AU MENU:"))

    elif choixmenu == "2":
         Montant = int(input("Entrer le montant:"))
         Numero = int(input("Entrer le numero de l'agent:"))
         print("Vous allez retirer", Montant, "F chez", Numero)
         print("1. Annuler")
         print("2. Confirmer")
    
         choixconfirm = input("Entrer votre choix:")

         if choixconfirm == "1":
            print("Merci Aurevoir")
         elif choixconfirm == "2":
             if Solde >= Montant:
                Solde -= Montant
                print("Votre retrait de", Montant, "F chez", Numero, "à bien été éffectué.\nVotre nouveau solde est de:",Solde)
             else:
                print("Votre solde est insuffisant pour effectuer ce retrait")
         else:
            print("Choix invalide, veuillez reesayer.")

         Retour = int(input("ENTRER 0 POUR ALLER AU MENU:"))

    elif choixmenu == "3":
         print("Le solde actuel de votre compte est:", Solde)

    elif choixmenu == "4":
         print("Merci Aurevoir")
         break

    else:
        print("Choix invalide, veuiller reesayer")