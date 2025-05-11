def guessing_game():
    correct_number = 6
    
    user_guess = int(input("Guess a number between 1 and 9: "))
    
    if user_guess < correct_number:
        print("Your guess is almost there!")
    elif user_guess > correct_number:
        print("Your guess is higher!")
    else:
        print("Your Guess Is Correct!")

guessing_game()
