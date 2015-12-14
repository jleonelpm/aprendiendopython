# -*- coding: utf-8 -*-

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide (a,b):
    try:
        return float(a/b)
    except:
        print "El resultado produce un error de división cero"