#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

annee = input("Saisissez une année : ")
annee = int(annee)

if annee % 400:
    print("Oui c'est claire elle est bissextile.")
else:
    print("Et non ! Elle n'est pas bissextile.")

