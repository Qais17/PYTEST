#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

annee = input()
try:
    annee = int(annee)
    if annee<=0:
        raise ValueError("l'année choisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide.")
