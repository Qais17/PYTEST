#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

try:
    resultat = numerateur / denominateur
except NameError:
    print("Variable numerateur ou denominateur non définie.")
except TypeError:
    print("Variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("Variable denominateur égale 0.")
else:
    print("Résultat obtenu", resultat)
