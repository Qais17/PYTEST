#!/usr/bin/python3.5
# -*-coding:Utf-8 -*
print("Salutation tete de naz, entre tes notes pour trouver ta moyen")
while 1:
    eleve = input("entre ton pseudo l'saligo: ")
    n1 = input("entre note ta de popculture: ")
    n1 = int(n1)
    n2 = input("entre ta note de sport: ")
    n2 = int(n2)
    n3 = input("entre ta note de entreprenariale: ")
    n3 = int(n3)
    n4 = input("entre ta note de creativiter: ")
    n4 = int(n4)
    n5 = input("entre ta note d'informatique: ")
    n5 = int(n5)
    total = n1 + n2 + n3 + n4 + n5
    moyen = total / 5
    print(eleve, ", tema ta moyen en yen : ", moyen)
    new = input("tu veux quitter l'saltimbanque ? si oui entre okay sinon on recommence: ")
    if new == "okay":
            print("Satisfait ?")
            break
