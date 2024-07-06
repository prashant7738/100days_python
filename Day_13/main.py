PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as letter_names:
    list_of_name = [name.strip() for name in letter_names.readlines()]


with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_data = starting_letter.read()
    for name in list_of_name:
        changed_data = letter_data.replace(PLACEHOLDER, name)
        with open(f"Output/{name}" , "w") as new_letter:
            new_letter.write(changed_data)

