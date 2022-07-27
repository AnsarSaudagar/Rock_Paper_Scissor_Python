from cpu_player import Cpu


opponent = Cpu()


game_on = True


while game_on:
    cpu_choice = opponent.generate_answer()
    player_choice = input(
        'Choose from ROCK PAPER AND SCISSOR OR WRITE END TO STOP THE GAME:\n').upper()
    if player_choice == 'ROCK' and cpu_choice == 'PAPER':
        print('You Lost')
    elif player_choice == 'ROCK' and cpu_choice == 'SCISSOR':
        print("You Won")
    elif player_choice == 'ROCK' and cpu_choice == 'ROCK':
        print('DRAW')
    elif player_choice == 'PAPER' and cpu_choice == 'PAPER':
        print('DRAW')
    elif player_choice == 'PAPER' and cpu_choice == 'SCISSOR':
        print("You Lost")
    elif player_choice == 'PAPER' and cpu_choice == 'ROCK':
        print('You Won')
    elif player_choice == 'SCISSOR' and cpu_choice == 'PAPER':
        print('You Won')
    elif player_choice == 'SCISSOR' and cpu_choice == 'SCISSOR':
        print("DRAW")
    elif player_choice == 'SCISSOR' and cpu_choice == 'ROCK':
        print('You Lost')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
