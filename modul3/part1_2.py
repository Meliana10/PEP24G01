#for
#
# my_str = 'Hello World'
# my_int = 100
#
# for letter in my_str:
#     print(letter)
#
# # for number in my_int: #int is not iterable
# #     print(number)
#
# for number in range(my_int):
#     print(number)

user_input = input('give string: ') #search x

for letter in user_input:
    if letter == 'x':
        continue
    print(letter)
else:
        print('x was not printed')


