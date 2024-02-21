# Un automat de cafea are următoarele opțiuni : Cappuccino, Espresso. Cappuccinocosta 4 lei,
# iar Espresso costa 3,5 lei. Aparatul de cafea accepta doar bancnote de 5 si 10 lei .
# Utilizatorului îi este afișat meniul, după care i se cere o opțiune. Dacă utilizatorul a
# introdus o opțiune validă, i se cere o bancnota. Dacă utilizatorul a introdus o bancnotă
# validă, acesta va primi restul și i se va livra produsul.
# Creați un script care sa simuleze acest automat de cafea în mod similar cu exemplul
# următor:
# 1. Cappuccino ... 4 lei
# 2. Espresso ...3.5 lei
# Ce optiune alegeti? [1,2]: 1
# Introduceti o bacnota [5,10]: 5
# Veti primi restul de 1 lei.
# Produsul se livreaza...

#METODA 1 REZOLVARE:
# print("MENIU: ")
# print("1. Cappuccino ... 4 lei")
# print("2. Espresso ... 3.5 lei \n")
#
# i = int(input("Ce optiune alegeti? [1,2]: "))
# j = int(input("Introduceti o bancnota [5, 10]: "))
#
# if i == 1 and j == 5:
#     print(f"Veti primi restul de {5 - 4} lei.")
# elif i == 2 and j ==5:
#     print(f"Veti primi restul de {5 - 3.5} lei.")
# elif i == 1 and j == 10:
#     print(f"Veti primi restul de {10 - 4} lei.")
# elif i == 2 and j == 10:
#     print(f"Veti primi restul de {10 - 3.5} lei.")
# print("Produsul se livreaza...")

#SAU METODA2 REZOLVARE:
print("1. Cappuccino ... 4 lei")
print("2. Espresso ... 3.5 lei \n")
products = {1: 4, 2: 3.5}
option = int(input("Ce optiune alegeti? [1,2]: "))
coin = int(input("Introduceti o bancnota [5, 10]: "))

# if option == 1:
#     product_value = 4
# elif option == 2:
#     product_value = 3.5
product_value = products[option]
for possible_coin in '5,10'.split(','):
    if coin == int(possible_coin):
            break
        # else:
        #     continue
else:
    print('not a valid coin')

print(f"Veti primi restul de {float(possible_coin)-float(product_value)} lei.")


