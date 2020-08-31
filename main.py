import random

play_game='yes'

while play_game == 'yes':
    answer =random.randint(1,100)
    print(answer)
    try_number=int(input('Guess a integer number between 1 and 10: '))


    while try_number != answer:
        if try_number>answer:
            print("The number is less than ",try_number)
        if try_number < answer:
            print("The number is greater than ",try_number)
        try_number = int(input('Guess a integer number between 1 and 10'))
    print("Congrats!...you have guessed the correct number")
    play_game= input("Do you want to play again?....type(yes/no)")


if play_game!='yes':
    print("ok,maybe next time")
