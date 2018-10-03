#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

annee = input("Entrer une année supérieure à 0 :")
try:
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Saisir un nombre uniquement.")
except AssertionError:
    print("Votre saisie est inférieure ou égale à 0.")
