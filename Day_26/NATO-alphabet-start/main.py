
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_word = {row.letter: row.code for (index,row) in data.iterrows()}
#print(phonetic_word)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter the word: ").upper()
output_lst = [phonetic_word[letter] for letter in word]
print(output_lst)
