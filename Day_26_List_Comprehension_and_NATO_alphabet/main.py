student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv('nato_phonetic_alphabet.csv')
letters = {row.letter: row.code for index, row in df.iterrows()}

while True:
    word = input("Enter a word: ")
    word_letters = [l for l in word]

    try:
        print([letters[letter.upper()] for letter in word_letters])
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
