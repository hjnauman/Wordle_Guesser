# Wordle_Guesser
This repository is a simple implementation to assist in guessing words while playing wordle.

## How it works
This program is a CLI tool for guessing wordle words. When ran you'll give the program your initial
guess and then the results of the guess with a formatted string that is displayed to the user. After
this step each round follows a similar process with each round providing the user with a recommended
suggestion based off each viable word's word frequency and multipliers for words that have only unique
letters.

## How to run
In order to run this tool clone this project and make sure you have python3 installed. From the root
directory of this tool simply run `py main.py` or `python main.py` dependending on how you have python
configured.
