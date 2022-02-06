from constants import LETTER_FREQUENCIES, VIABLE_WORDS
from letter import Letter


class Word():
    '''
    This class serves to keep track of the current word as the user progresses through the game. The word object holds many class methods that assist in the
    scripts execution. Additionally it hold the main data structure for the script which is a dict of letters with keys that represent the letters index in the
    word that you are guessing within wordle.
    '''
    def __init__(self):
        self.letters = {
            0: Letter(),
            1: Letter(),
            2: Letter(),
            3: Letter(),
            4: Letter()
        }

    def update_viable_words(self, invalid_char: str=None, index: int=None):
        '''
        This function is used to update the viable words list based on information about each letter guessed throughout the game. When an greyed out character
        is found we check to see if the index is pertinent. The index of the letter is pertinent when the letter has been verified in the word somewhere else
        during the current guess or previous guesses. If the letter hasn't been verified to exist within the word then we can remove all words that contain that
        letter, however, if the character does exist in the word then we can only remove words with the invalid char at the given index.

        Additional checks can be made based on the value of the word after guesses have been made. These TODO
        '''
        words_to_remove = set()

        # TODO: rewrite this entire function as there is duplicate logic
        if invalid_char is not None:
            check_index = False
            for letter in self.letters.values():
                if invalid_char == letter.verified_value:
                    check_index = True
                    break
                
                elif invalid_char in letter.verified_elsewhere:
                    check_index = True
                    break

            for word in VIABLE_WORDS:
                if check_index:
                    if invalid_char == word[index]:
                        words_to_remove.add(word)

                elif invalid_char in word:
                    words_to_remove.add(word)
        
        else:
            for word in VIABLE_WORDS:
                for index, letter_info in self.letters.items():
                    # verified letter doesn't match viable word
                    if letter_info.verified_value != '' and letter_info.verified_value != word[index]:
                        words_to_remove.add(word)
                        break
                    
                    # letter verified elsewhere in wrong spot or not in word
                    for char in letter_info.verified_elsewhere:
                        if char == word[index]:
                            words_to_remove.add(word)
                            break

                        elif char not in word:
                            words_to_remove.add(word)
                            break

        for word in words_to_remove:
            VIABLE_WORDS.remove(word)

    def update_word(self, guess: str, result: str):
        for i in range(5):
            if result[i] == '-':
                self.update_viable_words(guess[i], i)

            elif result[i] == 'g':
                self.letters[i].verified_value = guess[i]

            elif result[i] == 'y':
                self.letters[i].verified_elsewhere = guess[i]

            else:
                raise Exception(f'The result "{result[i]}" you gave is not formatted correctly.')

    def get_word_suggestion(self):
        '''
        This function creates a word suggestion based off of the user's previous guess data. This function first calculates a value for each viable word by
        summing the letter frequencies of each letter within the word. Additionally if a word contains all unique characters (meaning no duplicates) then the 
        words value gets a 2x multiplier because it should help eliminate more incorrect words from the viable words list. Whichever word has the best value is
        returned.
        '''
        best_suggestion = ''
        best_value = 0

        for word in VIABLE_WORDS:
            word_value = 0
            letter_tracker = []

            # increase word value by multiplier of two if each letter is unique
            multiplier = 2

            for char in word:
                word_value += LETTER_FREQUENCIES[char]

                # check for words that have duplicate letters and set multiplier to 1 if it does
                if char not in letter_tracker:
                    letter_tracker.append(char)
                else:
                    multiplier = 1

            word_value *= multiplier

            if word_value > best_value:
                best_value = word_value
                best_suggestion = word
        
        return best_suggestion
