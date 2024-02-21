# #Cereți input de la utilizator cu username și parola dorită. Se cere o funcție care sa
# verifice dacă are lungimea de minim 7 caractere, conține o cifra și una din următoarele
# caractere: !,@,%.
# Exemplu:
# Introduceti o parola: hcjdfhks
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Parola trebuie sa contina o cifra.
# Introduceti o parola: Iosido
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Parola trebuie sa contina o cifra.
# Parola trebuie sa aiba lungimea mai mare de 7 caractere.
# Introduceti o parola: Iosdis5
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Introduceti o parola: Isidjsdaj%3
# Parola este in regula.

def check_password():
    requires_chars = ["!", "@", "%"]
    password = input('Introduceti o parola: ')
    print(password)
    condition_not_ok = False
    if len(password) < 7:
        print("Parola cu lungime gresita")
        condition_not_ok = True

        for character in requires_chars:
            if character not in password:
                break
        else:
            print("Parola trebuie sa contina : ! @ %")
            condition_not_ok = True

        for character in range(10):
            if str(character) in password:
                break
        else:
            print("Parola trebuie sa contina number")
            condition_not_ok = True

        if condition_not_ok:
            check_password()

check_password()
