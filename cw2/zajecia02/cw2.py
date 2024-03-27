#Przypisania

dane = (2024, 'Python', 3.8)

rok, jezyk, wersja = dane
print(f'rok :{rok}, jezyk :{jezyk}, wersja :{wersja}')


oceny = [4, 3, 5, 2, 5, 4]

pierwsza, *srodek, ostatnia = oceny
print(f'pierwsza :{pierwsza}, srodek: {srodek}, wersja: {ostatnia}')

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

imie, nazwisko, _, _, zawod = info 

print(f'imie :{imie}, nazwisko: {nazwisko}, zawod: {zawod}')


dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, lista = dane
jezyk, wersja, opis = lista
print(f'rok :{rok}, jezyk: {jezyk}, wersja: {wersja}, opis: {opis}')

#Przypisania z wieloma celami i współdzielone referencje

a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(f'a :{a}, b :{b}')

c = a.copy()

c[0] = 'nowa wartość'

print(f'a :{a}, b :{b}, c : {c}')

x = y = 10
y = y + 1
print(f'x :{x}, y :{y}')

#Przypisania rozszerzone i współdzielone referencje

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(f'K :{K}, L :{L}, M : {M}, N : {N}')

#Techniki tworzenia pętli - uzupełnienie

imiona = ['Anna', 'Jan', 'Ewa'] 
oceny = [5, 4, 3]

pary = zip(imiona, oceny)

for para in pary:
    print(para)

print(f'pary :{pary}')

liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x**2

nowa_lista = list(map(kwadrat, liczby))

print(f'liczby : {liczby}, nowa_lista :{nowa_lista}')

#16

def zmien_wartosc(arg):
    if isinstance(arg, list): 
        arg[0] = 'kalafior'
    elif isinstance(arg, int): 
        arg = 65482652
    return arg

lista = [1, 2, 3]
print("Wartość przed wykonaniem funkcji:", lista)
print("Wartość po wykonaniu funkcji:", zmien_wartosc(lista))

liczba = 10
print("Wartość przed wykonaniem funkcji:", liczba)
print("Wartość po wykonaniu funkcji:", zmien_wartosc(liczba))

#17

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc_zamowienia = cena * ilosc
    podsumowanie = f"Nazwa produktu: {nazwa_produktu}, Cena: {cena} zł, Ilość: {ilosc}, Łączna cena: {wartosc_zamowienia} zł"
    return podsumowanie, wartosc_zamowienia

zamowienia = []

zamowienia.append(zamowienie_produktu("Chleb", cena=2, ilosc=3))
zamowienia.append(zamowienie_produktu("Mleko", cena=3.5))
zamowienia.append(zamowienie_produktu("Jajka", cena=0.5, ilosc=12))

for index, (podsumowanie, wartosc) in enumerate(zamowienia, start=1):
    print(f"Zamówienie {index}: {podsumowanie}")

suma_zamowien = sum(wartosc for _, wartosc in zamowienia)
print("Sumaryczna wartość zamówień:", suma_zamowien)

#18
def stworz_raport(*args, **kwargs):
    for id_produktu in args:
        print(f"Informacje o produkcie o ID {id_produktu}:")
        for key, value in kwargs.items():
            if str(id_produktu) in key:
                print(f"{key.split('_')[0]}: {value}")

stworz_raport(101, 102, nazwa_101='Kubek termiczny', cena_101='45.99 zł', nazwa_102='Długopis', cena_102='4.99 zł')

#19

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

#Użycie funkcji fabrykującej do stworzenia funkcji potęgującej
potega_2 = stworz_funkcje_potegujaca(2)

#Wywołanie funkcji potęgującej do kwadratu
print(potega_2(4)) 


#21 Adnotacje 

from typing import Callable

def licznik() -> Callable[[], int]:
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count

print(licznik())  
print(licznik())  

#22

ksiazki = [
    {'tytul': 'Harry Potter', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Wiedźmin', 'autor': 'Andrzej Sapkowski', 'rok_wydania': 1993},
    {'tytul': 'Game of Thrones', 'autor': 'George R.R. Martin', 'rok_wydania': 1996},
    {'tytul': 'The Hunger Games', 'autor': 'Suzanne Collins', 'rok_wydania': 2008},
    {'tytul': 'The Da Vinci Code', 'autor': 'Dan Brown', 'rok_wydania': 2003}
]

#a Sortowanie książek według roku wydania
posortowane_ksiazki = sorted(ksiazki, key=lambda x: x['rok_wydania'])
print("Książki posortowane według roku wydania:")
print(posortowane_ksiazki)

#b Filtracja książek wydanych po 2000 roku
ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))
print("\nKsiążki wydane po roku 2000:")
print(ksiazki_po_2000)

#c Transformacja listy do listy tytułów
tytuly_ksiazek = list(map(lambda x: x['tytul'], ksiazki))
print("\nTytuły książek:")
print(tytuly_ksiazek)

#23

def generator_dni_tygodnia():
    dni = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    for dzien in dni:
        yield dzien

print("Wszystkie dni tygodnia:")
for dzien in generator_dni_tygodnia():
    print(dzien)

print("\nPierwsze trzy dni tygodnia:")
pierwsze_trzy_dni = list(generator_dni_tygodnia())[:3]
print(pierwsze_trzy_dni)




