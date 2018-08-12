import os
import time
import game.numbers_interface
import game.letters_interface

def __main__():
    done = 0
    while done == 0:
        os.system('cls')
        choice = input('please select an option:\n (N)umbers \n (L)etters \n or (Q)uit\n')
        if choice.lower() == 'n':
            game.numbers_interface.numbers_game()
        elif choice.lower() == 'l':
            game.letters_interface.letters_game()
            time.sleep(3)
        elif choice.lower() == 'q':
            print('thank you ! come again')
            time.sleep(3)
            done = 1
        else:
            pass

# __main__()