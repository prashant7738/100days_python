import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_frame = pd.DataFrame(data)
# print(data_frame)

dict = {rows.letter : rows.code for (index ,rows) in data_frame.iterrows()}
# print(dict)


def generate_phonetic():
    word = input("Enter a word : ").upper()
    try:
        new_list = [dict[letter] for letter in word]
        
    except KeyError:
        print("Sorry we only take alphabets ")
        generate_phonetic()

    else:
        print(new_list)

generate_phonetic()