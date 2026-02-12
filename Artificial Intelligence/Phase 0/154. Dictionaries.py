# 🔹 Task 1: Number Frequency Counter
# Requirements:
# Take n numbers from user (allow duplicates)
# Store them in a list
# Create a dictionary that stores:
# number → frequency

def number_frequency_count():
    numbers = input("Enter the space separated numbers: ")
    nums_list = [int(i) for i in numbers.split()]

    dictionary = {}

    for num in nums_list:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    
    for k, v in dictionary.items():
        print(k, ":", v)




# 🔹 Task 2: Character Count in String
# Requirements:
# Take a string input
# Count frequency of each character
# Store result in dictionary

def character_count():
    string = input("Enter your string: ")
    dictionary = {}

    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    for k, v in dictionary.items():
        print(k, ":", v)



# 🔹 Task 3: Word Frequency Counter
# Requirements:
# Take a sentence as input
# Count frequency of each word
# Words separated by spaces

def Word_frequency_count():
    sentence = input("Enter sentence: ")
    words = sentence.split()

    dictionary = {}

    for string in words:
        if string in dictionary:
            dictionary[string] += 1
        else:
            dictionary[string] = 1
    
    for k, v in dictionary.items():
        print(k, ":", v)



def main_menu():
    while True:
        choice = int(input('''\nEnter your choice: 
    1. Number Frequencyy Count
    2. Character Count
    3. Word Frequency Count
    4. Exit.\n-> '''))
        
        if(choice == 1):
            number_frequency_count()
        elif (choice == 2):
            character_count()
        elif (choice == 3):
            Word_frequency_count()
        elif (choice == 4):
            exit()
        else:
            print("Invalid Choice!!")

main_menu()