# for i in range(10):
#      print(i)

#print(i)

#Exercitiu: Sa verificam daca unul dintre caracterele 2 si ! se afla in string

my_str = "abcde1232"
check_chars = ['2', '!']
for char_ in check_chars:
    if char_ in my_str:
        print(f"Success found: {char_}")
        break
else:
    print(f"Could not find any char in: {check_chars}")

my_str = "abcd1232"
check_chars = range(10)
for char_ in check_chars:
    print(f'success found: {char_}')
    break
