import json
import random
import os

# returns the absolute path from the main folder
def get_file_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(script_dir, filename)
    return main_path

# Laods the json file and return as dictionary
def load_file(filename):
    file_path = get_file_path(filename)
    with open (file_path, encoding="utf-8") as json_data:
        dic = json.load(json_data) 
        json_data.close()
        return dic
 
# Choose an random value from dictionary
def select_word_from_dict(file_load):
    _ , value = random.choice(list(file_load.items()))
    return value.lower()  

# verify if the name is the same
def validate_the_choice(choice_word,random_word, tries):
            if random_word == choice_word:
                print('you found the word !')

                return False
            if random_word != choice_word:
                print(f"Incorrect Word, try again {tries}/3")
                return True

def start_game():
    file_load = load_file('words.json')
    random_word = select_word_from_dict(file_load)
    tries, bool = 1, True
    for _ ,val in file_load.items():
        print('|',val.capitalize(),'|',end=' ')
    while (bool == True and tries <= 4):
        if (tries == 4):
            print(f'You lose, the correct word is: {random_word.capitalize()}')
            break
        else:
            choice_word = input("\nSelect an word from the list above: ").lower()
            bool = validate_the_choice(choice_word, random_word, tries)
            tries +=1

if __name__ == '__main__':
    start_game()

