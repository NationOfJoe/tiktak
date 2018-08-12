import os
import time
import random
import game.numbers_gam


def numbers_game():
    high_nums = [25,50,75,100]
    low_nums = [1,2,3,4,5,6,7,8,9,10]
    os.system('cls')
    j = 0
    quitted = 0
    h = 0
    digits = []
    while j != 6:
        print ('numbers drawn: {}'.format(','.join(str(x) for x in digits)))
        choice = input('select a (H)igh or (L)ow number\n you can always choose to (Q)uit\n')
        if choice.lower() == 'h':
            if h != 2:
                digit = random.choice(high_nums)
                digits.append(digit)
                print ('Number chosen {}\n'.format(digit))
                time.sleep(1)
                os.system('cls')
                h += 1
                j += 1
            else:
                print ('no more than 2 high numbers')
                time.sleep(2)
                os.system('cls')
        elif choice.lower() == 'l':
            digit = random.choice(low_nums)
            digits.append(digit)
            print('Number chosen {}\n'.format(digit))
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
        target = round(1000 * random.random(), 0)
        print('your numbers are {0}\nthe target is {1}\nyou have 40 seconds... good luck!\n'.format
               (
            ','.join(str(x) for x in digits),
            str(target).split('.')[0]
        )
               )

        time.sleep(5)
        for b in range(1,9):
            time.sleep(5)
            print('{} Seconds passed...\n'.format(str(b*5)))
        print('Time is up! now let me try ... \n')
        num_game = game.numbers_gam.numbers_game(digits, target)
        solution = num_game.solve()
        print('Best I got is {0}\n\nway to do it:\n {1}\n'.format(str(solution.answer).split('.')[0], solution.log))
        while True:
            last_input = input('press q to quit\n')
            if last_input.lower() == 'q':
                break