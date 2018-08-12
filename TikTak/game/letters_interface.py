import os
import time
import random

def letters_game():
    vowels= ['a', 'e', 'i', 'o', 'u']
    Eitzur= ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    os.system('cls')
    j = 0
    quitted = 0
    h = 0
    digits = []
    while j != 8:
        print ('letters drawn: {}'.format(','.join(str(x) for x in digits)))
        choice = input('select a (C)onstant or (V)owel \nyou can always choose to (Q)uit\n')
        if choice.lower() == 'v':
            if h != 3:
                digit = random.choice(vowels)
                digits.append(digit)
                print ('Letter chosen {}\n'.format(digit))
                time.sleep(1)
                os.system('cls')
                h += 1
                j += 1
            else:
                print ('no more than 3 Vowel letters')
                time.sleep(2)
                os.system('cls')
        elif choice.lower() == 'c':
            digit = random.choice(Eitzur)
            digits.append(digit)
            print('Letter chosen {}\n'.format(digit))
            time.sleep(2)
            os.system('cls')
            j += 1
        elif choice.lower() == 'q':
            quitted = 1
            break

        else:
            print('invalid selection! pick again')
            time.sleep(2)
            os.system('cls')
    if quitted == 0:
        print('your letters are {0}\nyou have 40 seconds... good luck!\n'.format(','.join(str(x) for x in digits)))
        time.sleep(5)
        for b in range(1,9):
            time.sleep(5)
            print('{} Seconds passed...\n'.format(str(b*5)))
        print('Time is up! now let me try ... \n')
        while True:
            last_input = input('press q to quit\n')
            if last_input.lower() == 'q':
                break