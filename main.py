import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

Phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input('enter a word').upper()
    try:
        output_list = [Phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letter in the alphabet please!")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

