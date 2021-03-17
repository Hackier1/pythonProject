#Zad1
a = [1-x for x in range(1,11)]
print(a)

b = [4**x for x in range(8)]
print(b)

c = [b for b in b if b % 2 == 0]
print(c)

#Zad2
import random
lista1 = [random.randint(10, 100) for x in range(10)]
lista2 = [lista1 for lista1 in lista1 if lista1%2==0]

print(lista1)
print(lista2)

################################################Zad3
#produkty = {"jajka": "sztuki",
#          "ziemniaki": "kg",
#          "banany": "kg"}
#produkty_kg = {}
#
#    produkty_kg[value] = "kg"
#
#Zad4
def trojkat(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 0
    if a+b<=c or b+c<=a or a+c<=b:
        return 0
    if b<=a and c<=a and (b**2)+(c**2)==(a**2):
        return 1
    if a <= b and c <= b and (a ** 2) + (c ** 2) == (b ** 2):
        return 1
    if a <= c and b <= c and (a ** 2) + (b ** 2) == (c ** 2):
        return 1
    else:
        return 0

print(trojkat(3,4,5))

#Zad5
def trapez(a=10,b=10,h=10):
    return ((a+b)*h)/2

print (trapez(1,2,3))

#Zad6
def ciag(a=1,b=4,ile=10):
    zwroc=1
    tablica = [a*b**x for x in range(ile)]
    print(tablica)
    licznik=0
    while licznik<10:
        zwroc = zwroc * tablica[licznik]
        licznik=licznik+1
    return zwroc

print(ciag())

#######################################################Zad7
#def ciag(* liczba):
#    if len(liczba) == 0:
#        return 0
#    else:
 #       suma = 0
 #       for i in liczba:
#            suma += i
 #           return suma
#print(ciag())
#print(ciag(1, 2, 3, 4, 5, 6, 7))