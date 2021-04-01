import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

Phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


word = input('enter a word').upper()

output_list = [Phonetic_dict[letter] for letter in word]
print(output_list)