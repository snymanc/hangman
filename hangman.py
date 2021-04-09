import random
import string
from words import words
from hangman_visual import hangmans_noose_dict


def get_valid_word(words):
    word = random.choice(words)  # random chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nUsed letters: ', ' '.join(used_letters))

        # current word (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(hangmans_noose_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1  # remove live
                print('Letter is not in the word.\n')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again?')

        else:
            print('\nInvalid character. Please try again?')

    # exits loop when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(hangmans_noose_dict[lives])
        print('You have been hanged! The word was', word)
    else:
        print('You live another day')


if __name__ == '__main__':
    hangman()
