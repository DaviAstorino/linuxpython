import os
from time import sleep
while True:
    n=input ("qual o seu nome? ")
    i=int(input ("qual a sua idade? "))
    print ("olá sr./a", n)
    print ("sua idade é:", i)
    if i<1:
        print ("você é recem-nascido")
    if i>0 and i<13:
        print ("você é criança")
    if i>12 and i<19:
        print ("você é jovem")
    if i>18 and i<61:
        print ("você é adulto")
    if i>60:
        print ("você é idoso")
    sleep (5)
    os.system('cls') 
