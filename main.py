import random

seven_letter_words = [
    "jupyter", "compile", "debug", "iterate", "package", "script",
    "integer", "boolean", "library", "control", "branch", "request",
    "conflict", "framework", "iterate", "request"
]

HANGMAN_PICS = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

def display(random_word, guessed_letters):
    # Display the current state of the guessed word
    underline = ''.join(c if c in guessed_letters else '_' for c in random_word)
    print(f"\nWord: {underline}")

def game_logic():
    random_word = random.choice(seven_letter_words)
    guessed_letters = set()
    attempts = len(HANGMAN_PICS) - 1

    print('Welcome to Hangman!')
    print('Guess the word: ', '_' * len(random_word))

    while attempts > 0:
        display(random_word, guessed_letters)
        print(HANGMAN_PICS[len(HANGMAN_PICS) - attempts - 1])
        user_guess = input('Enter a letter: ').lower()

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue
        if user_guess in guessed_letters:
            print('You already picked that letter, choose a new one.')
        elif user_guess in random_word:
            guessed_letters.add(user_guess)
            print(f"Good guess! '{user_guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
            guessed_letters.add(user_guess)

        if set(random_word) == guessed_letters:
            display(random_word, guessed_letters)
            print(f'Congratulations! You won the game! The word was: {random_word}')
            break

        if attempts == 0:
            print(f'Sorry, you lost! The word was: {random_word}')

    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again == 'y':
        game_logic()
    else:
        print("Thanks for playing!")

game_logic()
