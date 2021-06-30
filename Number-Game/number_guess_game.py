import random

def rules():
    rules_decision = input("Type 'yes' or 'y' if you want to read the rules.\nType anything else otherwise: ")
    if rules_decision.lower() in ['y', 'yes']:
        print("""\nWelcome to The Number Guessing Game!
In this game, a random number will be choseen from 0 to 100.
It is your goal to get as close to that number as possible.
You will start out with 200 points, and every time you make 
a guess you lose 10 points. You get 5 guesses total. 
At the end of the 5th guess, you will lose 2 points for every 
number between your last guess and the real number. 
There is a shop where you can spend your points to get hints.
You can type 'shop' at any point before a guess to access the shop.
In the shop, you can spend 20 points to learn if the number is higher
or lower than your guess. You can spend 10 points to learn if it is
divisible by a number of your choosing. At any point after you make
a guess, you can type 'confirm' to confirm your guess. This will
make it as if you used your 5th turn, but you will not lose points
for the rounds you have skipped. You will lose 4 points for every
integer you are off by. You can type 'points' after making a guess
and you will be told your points. If you guess the number, 
you will be prompted and told your points. After the game, you will
be able to play again. You can also see the highest score you recieved
across your runs and the average score you recieved. You can also use the
first letter of each command to input it.""")
    return


def confirm(guessed_number, give_up):
    if guessed_number in ['']:
        print('Make a guess first')
    else:
        give_up = True
    return give_up


def guess_or_invalid(decision, points, guesses, real_number, give_up, guessed_number):
    try:
        int(decision)
        if int(decision) in range(101):
            guessed_number = int(decision)
            if (guessed_number != real_number):
                points -= 10
                guesses += 1
            else: 
                print("\nYou guessed it!")
                give_up = True
        else:
            print("That is not in the range of 0 to 100")
    except ValueError:
        print("That is not a valid input")
    return points, guesses, give_up, guessed_number


def shop(points, guessed_number, real_number):
    decision = input("""\nWould you like to buy a higher or lower hint or divisor hint?
Type '1' for higher or lower hint
Type '2' for divisor hint\n""")
    if decision in ['1']:
        if guessed_number in ['']:
            print("You have to take a guess before doing a higher or lower hint\n")
        else:
            points -= 20
            if guessed_number > real_number:
                print("The real number is lower than your guess\n")
            else:
                print("The real number is higher than your guess\n")
    elif decision in ['2']:
        points -= 10
        divisor = int(input("What number would you like to try and divid the real numebr by?\n"))
        if (real_number % divisor == 0):
            print("The real number is dividible by " + str(divisor))
        else:
            print("The real number is not dividible by " + str(divisor))
    else: print("That is not a valid input\n")
    return points


def play_again(continue_playing):
    decision = input("Would you like to play again? Type 'y or 'yes' if you wish to.\n")
    if decision in ['y', 'yes']:
        pass
    else:
        continue_playing = False
    return continue_playing


def game_body():       
    number_guesses = 4
    guessed_number = ''
    real_number = random.randint(1, 100)
    guesses = 0
    points = 200
    give_up = False
    while number_guesses >= guesses and not(give_up):
        decision = input("Type a guess between 0 and 100, 'shop', 'points' or 'confirm': ")
        if decision.lower() in ['shop']:
            points = shop(points, guessed_number, real_number)
        elif decision.lower() in ['confirm']:
            give_up = confirm(guessed_number, give_up)
        elif decision.lower() in ['points']:
            print("\nYou have " + str(points) + " points")
        else: points, guesses, give_up, guessed_number = guess_or_invalid(decision, points, guesses, real_number, give_up, guessed_number)
    difference = abs(guessed_number - real_number)
    points -= 2*difference
    if points < 0:
        points = 0
    print("\nYou got " + str(points) + " points.")
    return points


def high_score_or_average(point_list, iterations):
    
    decision = input("""Would you like to see your average score and high score?
Type 'yes' or 'y' to see your average and high score:\t""")
    if decision in ['y', 'yes']:
        average = (sum(point_list)/iterations)
        print("Your average is " + str(average) + "!")
        print("Your high score is " + str(max(point_list)) + "!")
    return


if __name__ == '__main__':
    continue_playing = True
    point_list = []
    iterations = 0
    rules()
    while continue_playing is True:
        iterations += 1
        point_list.append(game_body())
        high_score_or_average(point_list, iterations)
        continue_playing = play_again(continue_playing)
