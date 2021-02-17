import random


while True:
    pass_len = input('number of characters: ')
    password = ''
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVYZabcdefghijklmnopqrstuvyz0123456789@#&'
    symb_len = len(symbols)
    pass_len = int(pass_len) 

    for i in range(pass_len):
        password += symbols[random.randrange(symb_len-1)]

    print(password)
    
    response = input('Quit y/n ?: ')

    if response == 'y':
        break