#METODA1
parola = 7788

while True:
    parola_introdusa = int(input('Introduceti parola:'))
    if parola == parola_introdusa:
        print("Acces permis! ")
        break
    else:
        print("Parola gresita. Mai incearca.")

#METODA 2
# if i == parola:
#     print("Acces permis.")
# else:
#     print("Parola gresita. Mai incercati.")



#METODA3
# parola = 7788
#
# for incercare in range(99999):
#     parola_introdusa = int(input('Introduceti parola: '))
#     if parola == parola_introdusa:
#         print("Acces granted")
#         break
#     else:
#         print("Parola gresita.")
