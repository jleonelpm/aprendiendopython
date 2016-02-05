# -*- coding: utf-8 -*-
print "Este programa fue realizado por mi"
elefantes = int(raw_input("Cuantos elefantes"))
cant_elefantes = 0
while elefantes > cant_elefantes:
    cant_elefantes = cant_elefantes +1
    if cant_elefantes == 1:
        print "1 elefante se columpiaba sobre la tela de la araña"
    else:
        print cant_elefantes, "elefantes se columpiaban sobre la tela de la araña"
