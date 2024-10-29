#Librerias importadas de python
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Primera parte: Solicitar el número de vectores con el que se va a trabajar.
print("\033[1;34m"+"\n¡Bienvenido al programa de vectores de XFORCE!"+"\033[0;m"+"\n\n¿Con cuántos vectores (n) deseas trabajar?")
numvectors=input("\033[1;32m"+"n= "+"\033[0;m")
while not(numvectors.isdigit()) or not(int(numvectors)>0):
    print("\033[1;31m"+"**"+"\033[4;30m"+ "Lo sentimos, lo que has ingresado no es un número valido, vuelve a intentarlo"+"\033[0;m")
    numvectors= input("\033[1;32m"+"n= "+"\033[0;m")

#Segunda parte: Definir la información que me dará de cada vector y almacenarlo.
vectoresinfo=[]
opValInfo=["a","b","c","1","2"]
for i in range (int(numvectors)):
    infoVectori=[i+1]
