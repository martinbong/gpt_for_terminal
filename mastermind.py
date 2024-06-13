import random

# Opening message
def welcome_message():
    print("Welcome to MASTERMIND ('x' = Game Over)")

# Determines the game's difficulty based on user choice (default: 4, 6, 12)
def rules():
    while True:
        choice = input("Default rules? (y/n): ").strip().lower()
        if choice == 'x':
            print("Game Over")
            quit()
        elif choice in ['yes', 'y']:
            positions = 4
            options = 6
            guesses = 12
            break
        elif choice in ['no', 'n']:
            positions = get_valid_input("Enter the number of positions (1-10, default = 4): ", 1, 10)
            options = get_valid_input("Enter the number of options (2-10, default = 6): ", 2, 10)
            guesses = get_valid_input("Enter the number of guesses (5-40, default = 12): ", 5, 40)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return positions, options, guesses

# Helper function to get valid input within a range
def get_valid_input(prompt, min_val, max_val):
    while True:
        value = input(prompt).strip().lower()
        if value == 'x':
            print("Game Over")
            quit()
        try:
            value = int(value)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Creates a list of all options called 'letters' (letters instead of colors) (e.g. 6 positions means A-F)
def colors(options):
    all_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = []
    for i in all_options:
        if options != 0:
            letters.append(i)
            options -= 1
    return letters

# Generates a code of length 'positions' in random range 'letters' (e.g. ['D', 'B', 'D', 'C'])
def code_generator(positions, letters):
    code = []
    while positions != 0:
        code.append(None)
        positions -= 1
    for i in range(len(code)):
        code[i] = random.choice(letters)
    return code

# Creates a dictionary of 'letters' and how often they occur in 'code' (e.g. {A:2, B:0 etc.})
def code_dict(letters, code):
    code_d = {}
    for i in letters:
        code_d[i] = code_d.get(i, 0)
    for i in code:
        if i in code_d:
            code_d[i] += 1
    return code_d

# Allows the user to input a 'guess' (e.g. for 4 positions: dbdc)
def input_guess():
    inputs = str(input("> ").upper())
    if inputs == 'X':
        print("Game Over")
        quit()
    guess = []
    for i in inputs:
        guess.append(i)
    return guess

# Checks if 'guess' is of the same length as 'code' and contains entries occurring in 'letters' only
def input_check(guess, code, letters):
    check = 0
    for i in guess:
        if i not in letters:
            check += 1
    if len(guess) != len(code) or check != 0:
        print("Invalid guess.")
        return False
    else:
        return True

# Creates a dictionary of 'letters' and how often they occur in 'guess' (e.g. {A:2, B:0 etc.})
def guess_dict(letters, guess):
    guess_d = {}
    for i in letters:
        guess_d[i] = guess_d.get(i, 0)
    for i in guess:
        if i in guess_d:
            guess_d[i] += 1
    return guess_d

# Checks the number of correct positions in 'guess' as compared to 'code'
def correct_positions(code, guess):
    corr_pos = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:
            corr_pos += 1
    return corr_pos

# Checks the number of correct colors in 'guess' as compared to 'code' that are not in their correct positions
def correct_colors(code_d, guess_d, corr_pos):
    corr_col = 0
    for i in code_d:
        if code_d[i] <= guess_d[i]:
            corr_col += code_d[i]
        elif code_d[i] > guess_d[i]:
            corr_col += guess_d[i]
    corr_col -= corr_pos
    return corr_col

# When the user wins
def win(guesses_left, guesses, code):
    guesses_left -= 1
    print("CODE " + str(code) + " CRACKED" " with " + str(guesses_left) + "/" + str(guesses) +
          " guesses left!")
    quit()

# When the user loses
def lose(code):
    print("YOU LOSE! The correct code was " + str(code))
    quit()

# The game-loop, the program keeps asking the user's input until the win or lose condition is met
def game_loop(code, letters, code_d, guesses_left, guesses):
    turn = 0

    while guesses_left != 0:

        guess = input_guess()
        while not input_check(guess, code, letters):
            guess = input_guess()

        guess_d = guess_dict(letters, guess)

        if guess != code:
            corr_pos = correct_positions(code, guess)
            corr_col = correct_colors(code_d, guess_d, corr_pos)
            guesses_left -= 1
            turn += 1
            print(str(turn) + ".\t" + str(guess) + " has " + str(corr_pos) + " correctly positioned letters and " +
                  str(corr_col) + " incorrectly positioned letters. " + str(guesses_left) + "/" + str(guesses) +
                  " guesses left.")
        else:
            win(guesses_left, guesses, code)
            quit()

    lose(code)
    quit()

# Connects all functions in the right order
def mastermind():
    welcome_message()
    positions, options, guesses = rules()
    letters = colors(options)
    guesses_left = guesses
    code = code_generator(positions, letters)
    code_d = code_dict(letters, code)
    print("A code has been generated with " + str(positions) + " letters (" + str(letters[0]) +
          "-" + str(letters[len(letters) - 1]) + ")\nPlease take a guess...")
    game_loop(code, letters, code_d, guesses_left, guesses)

mastermind()
