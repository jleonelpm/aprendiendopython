# -*- coding: utf-8 -*-

#print '----------------------'
print 'a. Abrir un archivo'
print 'c. Crear un archivo'
print 's. Salir\n'
#print '---------------------'

opcion = raw_input ('Selecciona tu opcion;\n')

if opcion == 'a':
    que_archivo = raw_input ('Introduce el nombre del archivo:')
    try:
        archivo = open (que_archivo)
        contador = 0
        for linea in archivo:
            print linea
    except:
        print "El archivo que intentas abrir no existe"
        quit()
elif opcion =='c':
    que_archivo = raw_input ('Introduce el nombre del archivo:')
    try:
        archivo = open (que_archivo,'w')
        linea1 = "linea 1: Archivo creado por leonel\n"
        archivo.write(linea1)
        linea2 = "linea 2: Se ha escrito una segunda línea\n"
        archivo.write(linea2)
        archivo.close()
        print "Archivo creado con éxito"
    except:
        print "Se produjo un error al crear el archivo"
        quit()
else :
    print 'salir'