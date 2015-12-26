# -*- coding: utf-8 -*-
import socket

#EJEMPLO DE UNA CONEXION A TRAVES DE TCP

host = "itsva.edu.mx"
puerto = 80
# crear un objecot socket de IPV4 (AF_INET) para TCP (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conexión al cliente
client.connect((host,puerto))
# Solicitud de la petición
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# Recepción de la respueta y su impresión
response = client.recv(4096)
print response

# EJEMPLO DE UNA CONEXIÓN A TRAVÉS DE UDP

host = "127.0.0.1"
puerto = 15000
# crear un objecot socket de IPV4 (AF_INET) para UDP (SOCK_DGRAM)
conexion = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
conexion.bind((host,puerto)) #Se crea una conexión en modo escucha
while True:
    data, addr = conexion.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data