import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_frame = pd.DataFrame(data)
# print(data_frame)

dict = {rows.letter : rows.code for (index ,rows) in data_frame.iterrows()}
# print(dict)

word = input("Enter a word : ").upper()
list_of_letter = [letter for letter in word]
# print(list_of_letter)

new_list = [dict[letter] for letter in list_of_letter]

print(new_list)