# #zad1
# def foo(imie, nazwisko):
#         wynik=imie+'. '+nazwisko
#         return wynik
# imie='M'
# nazwisko='Senderowski'
# print(foo(imie,nazwisko))

# #zad2
# def foo(imie, nazwisko):
#         imie1=imie[0].upper()
#         wynik=imie1+'. '+nazwisko[0].upper()+nazwisko[1:len(nazwisko)]
#         return wynik
# imie='mateusz'
# nazwisko='senderowski'
# print(foo(imie,nazwisko))

# #zad3
# def foo(pierwsze,drugie,wiek):
#     rok_u=0
#     rok_u+=pierwsze*100
#     rok_u+=drugie
#     rok_u-=wiek
#     return rok_u
# print(foo(20,21,22))

# #zad4
# def foo(imie,nazwisko):
#     wynik=poprawny_zapis(imie,nazwisko)
#     return wynik
#
# def poprawny_zapis(imie, nazwisko):
#     imie1 = imie[0].upper()
#     wynik = imie1 + '. ' + nazwisko[0].upper() + nazwisko[1:len(nazwisko)]
#     return wynik
#
# imie='mateusz'
# nazwisko='senderowski'
# print(foo(imie,nazwisko))

# #zad5
# def foo(a,b):
#     wynik=0
#     if(a>0 and b>0 and b!=0):
#         wynik = a / b
#     return wynik
#
# print(foo(2,4))

# #zad6
# def foo():
#     i=0
#     while i<100:
#         i=i+int(input('Podaj liczbe: '))
#         print('Suma = ',i)
#     return 0
# foo()

# #zad7
# def foo(lista):
#     wynik=(lista[0])
#     return wynik
# lista=['a']
# print(foo(lista))

# #zad8
# lista=[]
# for i in range(5):
#     lista.append(input())
# krotka=tuple(lista)
# print(krotka)

# #zad9
# def foo(dzien):
#     dnie = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
#     return dnie[dzien-1]
# print(foo(6))

# #zad10
# def foo(lista):
#     lista2=lista.copy()
#     lista2.reverse()
#     for i in range(len(lista)):
#         if(lista[i]!=lista2[i]):
#             return 0
#     return 1
# lista=['x','a','n','a','x']
# if(foo(lista)==1):
#     print('Lista jest palindromem')
# else:
#     print('Lista nie jest palindromem')