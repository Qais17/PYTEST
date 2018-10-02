#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

i = 1
while i < 20:
     if i % 3 == 0:
             i += 4
             print("On incrémente i de 4. i est maintenant egale a", i)
             continue
     print("la variable i =", i)
     i += 1
