#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

chaine = input("écrivez ce que vous voulez: ")
for lettre in chaine:
     if lettre in "AEIOUYaeiouy":
             print (lettre)
     else:
            print("*")

