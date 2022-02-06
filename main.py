from constants import VIABLE_WORDS
from word import Word

if __name__ == "__main__":
    current_word = Word()

    # Get initial guess and present user with result format
    guess = input('Please type your initial guess:\n').lower()

    print('\nPlease type your result:')
    print('    ("-" represents an unknown letter)')
    print('    ("G" represents a known letter)')
    print('    ("Y" represents a letter elswhere in the word)')
    print('    Ex: -GGY-')

    result = [x for x in input().lower()]

    # Initiate remaining rounds
    for i in range(5):
        # Update word and viable words and then get recommended suggestion
        current_word.update_word(guess, result)
        current_word.update_viable_words()
        suggestion = current_word.get_word_suggestion()

        # Give user information about remaining possible words and prompt for next guess
        print(f'\nThere are {len(VIABLE_WORDS)} possible words left.')

        # If the viable words contain 10 or less words print these words
        if len(VIABLE_WORDS) <= 10:
            print('These are the remaining words:')
            for word in VIABLE_WORDS:
                print(f'    {word}')
        
        # Give the user the suggested word and get their guess and result values
        print(f'From these possible words our suggested word is: {suggestion}.')
        guess = input('\nPlease type your next guess:\n').lower()
        result = [x for x in input('\nPlease type your result:\n').lower()]

