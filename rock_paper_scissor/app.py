import random

rules = 'Rules:\nRock beats Scissor\nScissor beats Paper\nPaper beats Rock\n'

def start_choice() -> int:
    while True:
        try:
            s_choice = int(input('1-Play the game\n2-Rules\n3-Quit\nChoose one of the following options: '))
            
            if s_choice in (1, 2, 3):
                return s_choice
            else:
                print('Select one of the specified values')
            
        except ValueError:
            print('Selected value is not a number')

def player_choice() -> int:
    while True:
        try:
            p_choice = int(input('1-Rock\n2-Scissor\n3-Paper\nChoose an option: '))
            
            if p_choice in (1, 2, 3):
                return p_choice
            else:
                print('Select one of the specified values')
            
        except ValueError:
            print('Selected value is not a number')
            
def cpu_choice() -> int:
    c_choice = random.randint(1, 3)
    
    if c_choice == 1:
        print('CPU choice: Rock\n')
    elif c_choice == 2:
        print('CPU choice: Scissor\n')
    elif c_choice == 3:
        print('CPU choice: Paper\n')
    return c_choice

def main_game() -> int:
    while True:
        p_choice = player_choice()
        c_choice = cpu_choice()
      
        if p_choice == c_choice:
            print('Draw!\nTry again!\n')
        elif (p_choice == 1 and c_choice == 2) or \
             (p_choice == 2 and c_choice == 3) or \
             (p_choice == 3 and c_choice == 1):
            print('You won!')
            break
        else:
            print('You lost')
            break

def main():
    while True:
        print('Welcome to Rock/Paper/Scissors!')
        s_choice = start_choice()
        
        if s_choice == 1:
            main_game()
            while True:
                play_again = input('\nPlay again? (y/n): ').lower()
                
                if play_again in ('y', 'yes'):
                    break
                elif play_again in ('n', 'no'):
                    return
                else:
                    print('Choose one of the available options')
            
        elif s_choice == 2:
            print(rules)
            
        elif s_choice == 3:
            print('Good bye!')
            break
        
if __name__ == '__main__':
    main()
