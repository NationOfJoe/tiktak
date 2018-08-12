import os
import time
import random

def letters_game():
    Ehevi_letters = ['ה','א','ו','י']
    Eitzur= ['ב','ג','ד','ז','ח','ט','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']
    os.system('cls')
    j = 0
    quitted = 0
    h = 0
    digits = []
    while j != 8:
        print ('letters drawn: {}'.format(','.join(str(x) for x in digits)))
        choice = input('select a (E)itzur or (V)aule letter\n you can always choose to (Q)uit\n')
        if choice.lower() == 'v':
            if h != 3:
                digit = random.choice(Ehevi_letters)
                digits.append(digit)
                print ('Letter chosen {}\n'.format(digit))
                time.sleep(1)
                os.system('cls')
                h += 1
                j += 1
            else:
                print ('no more than 3 EHEVI letters')
                time.sleep(2)
                os.system('cls')
        elif choice.lower() == 'e':
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
        time.sleep(5)