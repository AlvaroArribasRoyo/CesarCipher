#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
def cesar(alfabeto,texto,modo):
    """list,string,string -->void
    Controlar que el modo solo sea c o d"""
    resFinal=""
    for u in range (0,len(alfabeto)):
        resultado=""
        for i in range(0,len(texto)):
            letra=texto[i]
            posicion=busqueda(alfabeto,letra)
            if modo=="-c" and posicion!=-1:
                resultado+=alfabeto[(posicion+u)%len(alfabeto)]
            elif modo=="-d" and posicion!=-1:
                resultado+=alfabeto[(posicion-u+len(alfabeto))%len(alfabeto)]
            else:
                resultado+=letra
        resFinal+="Transposicion "+str(u)+": "+resultado+"\n"
    return resFinal

def busqueda(alfabeto,letra):
    for j in range(0,len(alfabeto)):
        if letra.upper()==alfabeto[j]:
            return j
    return -1

def usage():
    print("Usage:cesar.py -c/d -e/-s fileSource.txt fileTarget.txt")
    print("-c\t\tencode text\n-d\t\tdecipher text\n-s\t\tspanish\n-e\t\tenglish\n")

def escribirArchivo(nombre,texto):
    archivo=open(nombre,'w')
    archivo.write(texto)
    archivo.close
    
def leerArchivo(nombre):
    archivo=open(nombre,'r')
    lineas=""
    for linea in archivo:
        lineas+=linea
        #Elimina el salto de linea
        sinSalto=lineas.split("\n")
        lineas=str(sinSalto[0])
        lineas+=" "
    archivo.close()
    return lineas

def programaPrincipal(sysop):
    if sysop=="nt":##Para Windows
        lineas=""
        texto=""
        modo=sys.argv[1]
        idioma=sys.argv[2]
        entrada=sys.argv[3]
        salida=sys.argv[4]
        if modo!="-help":
            try:
                lineas=leerArchivo(entrada)
                if modo.lower()=="-c" or modo.lower()=="-d":
                    if idioma.lower()=="-s":
                        texto=cesar(spanish,lineas,modo)
                    elif idioma.lower()=="-e":
                        texto=cesar(english,lineas,modo)
                    else:
                        print("Error to select language: \n-e/-s")
                    escribirArchivo(salida,texto)
                else:
                    print("Error to encode or cypher: -c/-d")
            except:
                print("Error.The file doesn't match")
        else:
            usage()
    else:##Para linux
        modo=sys.argv[2]
        idioma=sys.argv[3]
        entrada=sys.argv[4]
        salida=sys.argv[5]
        if modo!="-help":
            try:
                lineas=leerArchivo(entrada)
                if modo.lower()=="-c" or modo.lower()=="-d":
                    if idioma.lower()=="-s":
                        texto=cesar(spanish,lineas,modo)
                    elif idioma.lower()=="-e":
                        texto=cesar(english,lineas,modo)
                    else:
                        print("Error to select language: \n-e/-s")
                        print(texto)
                    escribirArchivo(salida,texto)
                else:
                    print("Error to encode or cypher: -c/-d")
            except:
                print("Error.The file doesn't match")
        else:
            usage()
        
##Programa principal##
spanish=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ã‘','O','P','Q','R','S','T','U','V','W','X','Y','Z')
english=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
sysop=os.name
parametros=len(sys.argv)
if (sysop=="nt" and parametros!=5) or (sysop=="posix" and parametros!=6):
    usage()
elif (sysop=="nt" and parametros==5) or (sysop=="posix" and parametros==6):
    programaPrincipal(sysop)
else:
    print("Operating system not supported")



