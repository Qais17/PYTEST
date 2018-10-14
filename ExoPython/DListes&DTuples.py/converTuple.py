#!/usr/bin/python3.5
# -*-coding:Utf-8 -

def afficher(*parametres, sep=' ', fin='\n'):
""" L'objectif ici, c'est d'imiter l'attitude de print. """
    parametres = list(parametres)
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    chaine = sep.join(parametres)
    chaine += fin
    print(chaine, end='')
