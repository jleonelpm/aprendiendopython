# -*- coding: utf-8 -*-
import random

n = int(raw_input("Cantidad de numeros aleatorios a generar"))
for i in range(n):
    x = int (random.randint(1,100))
    print x

vocales = ["a","e","i","o","u"]
vocal_rand = random.choice(vocales)
vocal_in = raw_input("Adivina la vocal: ")
if vocal_rand == vocal_in:
    print "Hurra, adivinaste la vocal"
else:
    print "Upsss, la vocal era ", vocal_rand