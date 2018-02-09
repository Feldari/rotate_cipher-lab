#!/usr/bin/env python3.6


def encode():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot_count = abs(int(input('How many letters to shift? ')))
    user_in = input('What string to encode?: ').upper()
    print('\nYour code: ')
    user_out = ''
    alpha_index = 0
    for letter in user_in:
        if letter == ' ':
            pass
        else:
            alpha_index = alphabet.find(letter) 
            shift_value = (alpha_index + rot_count) % 26
            user_out = user_out + alphabet[shift_value]

    return user_out

def decode():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot_count = abs(int(input('How many letters to shift? ')))
    user_in = input('What string to decode?: \n').upper()
    print('\nYour plaintext: ')
    user_out = ''
    alpha_index = 0
    for letter in user_in:
        if letter == ' ':
            pass
        else:
            alpha_index = alphabet.find(letter) 
            shift_value = (alpha_index - rot_count) % 26
            user_out = user_out + alphabet[shift_value]

    return user_out


if __name__ == '__main__':
    while True:
        print('Rotational Encoder / Decoder Menu: ')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        select = input('Enter number from menu: ')

        if select == '1' or select.upper() == 'ENCODE':
            print(encode())
            print()
        elif select == '2' or select.upper() == 'DECODE':
            print(decode())
            print()
        elif select == '3' or select.upper() == 'EXIT':
            break
        else:
            print('Please select an item from the menu!\n')
