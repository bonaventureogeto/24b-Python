import random
words = ['funny', 'absurd', 'buffalo', 'jackpot', 'uptown', 'scratch']
correct_word = random.choice(words).upper()
display_word = '_' * len(correct_word)
turns = 6
guess_letters = []
while turns > 0:
    guess = input('Guess a letter: ').upper()
    if guess in guess_letters:
        print('Oops! You have already guessed that letter.')
        continue
    guess_letters.append(guess)
    if guess in correct_word:
        print('Correct! The letter is part of the word.')
        new_displayed_word = ''
        for i in range(len(correct_word)):
            if correct_word[i] == guess:
                new_displayed_word += guess
            else:
                new_displayed_word += display_word[i]
        display_word = new_displayed_word
    else:
        turns -= 1
        print(f'Incorrect. {turns} turns remaining.')
    if '_' not in display_word:
        print('Congratulations! You won.')
        break
if turns == 0:
    print('Sorry, you lost.')
