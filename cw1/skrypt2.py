import math
import random

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
lista = [1,2,3,4,5]
losowa = random.choice(lista)


tekst = "Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])

print(tekst.upper())

tekst = tekst.replace(tekst[2], 'p')
print(tekst)


lista = list(tekst)

lista = lista[0:8]
#print(lista)

lista2 =  [1,2,3,4,5]

lista = lista + lista2
print(lista)

lista.remove(":")
print(lista)


lista2 = [1,2,3,"banan",100]
print(f'Lista2: {lista2}')
lista3 = []
for element in lista2:
    if isinstance(element, int):
       lista3.append(element**2)

lista3 = [x**2 for x in lista2 if x != "banan"]

print(f'Lista3: {lista3}')

lista4 = [x for x in range(2, 17, 2)]

print(f'Lista4: {lista4}')

#slowniki

ja = {
    "imie": "Piotr",
    "nazwisko": "Cięgotura",
    "wiek": 26,
    "rodzice": [
        {"imie": "Tomasz", "wiek": 59},
        {"imie": "Kamila", "wiek": 58}
    ]
}

print(ja["rodzice"])
print(ja["rodzice"][0]["imie"])
print(ja.keys())
print("rodzenstwo" in ja)

#krotki

krotka1 = (1, 2, "3", 4, 2, 5)

print(f'Dlugosc: {len(krotka1)} pierwszy wyraz: {krotka1[0]}')
print(f'Wartosc 2 wystepuje {krotka1.count(2)} razy')

nowa_krotka = (2,) + krotka1[1:]

#zbiory

X = set("kalarepa") 
Y= set("lepy")

print(f'{X & Y}')

#instrukcje
'''
imiona = ["Anna", "Jan", "Katarzyna", "Tomasz"]

for indeks, imie in enumerate(imiona):
    print("Indeks:", indeks, ", Imię:", imie)

liczba = 6

if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest dodatnia i parzysta")

liczba = int(input("Podaj liczbę: "))

if liczba != 0:
    print("Liczba jest różna od zera")

dostepne_owoce = ['jabłko', 'banan', 'pomarańcza']
owoc = input("Podaj nazwę owocu: ")

if owoc in dostepne_owoce:
    print("Owoc jest dostępny")

suma = 0

while suma <= 100:
    liczba = int(input("Podaj liczbę: "))
    suma += liczba

print("Suma wprowadzonych liczb wynosi:", suma)'''

#dziwactwa

#1. Przypisanie tworzy referencje, a nie kopie
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

#2. Powtórzenie dodaje jeden poziom zagłębienia
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")
