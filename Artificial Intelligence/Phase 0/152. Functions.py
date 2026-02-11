# Write functions for: palindrome check, string reverse, vowel count, word count

# Palindrome Check function
def palindrome_check(x):
    orig = x
    y=0
    while(x>0):
        y = y * 10 + x % 10
        x //= 10
    return orig == y


# String Reverse function
def str_reverse(str1):
    str1 = str[::-1]
    return str1


# Vowel Count
def vowel_count(str2):
    vowels = 0
    for i in str2:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels+=1
    return vowels


# Words Count
def word_count(str3):
    count = 0
    str3 = str3.split()
    for i in str3:
        count += 1
    return count


# Main Menu
def main_menu():
    print("""Choose what to do by entering number:
    1. Check if number is palindrome?
    2. Reverse the string.
    3. Count the number of vowels in the stirng.
    4. Count the number of words in the string.
    5. Exit.""")
    
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        num = int(input("Enter number to check if palindrome: "))
        result = palindrome_check(num)
        if (result):
            print("Entered number is palindrome.")
        else:
            print("Entered number is not palindrome.")
        main_menu()
    
    elif (choice == 2):
        string = input("Enter the string you want to reverse: ")
        reversed_str = str_reverse(string)
        print("Your String: %s\nReversed String: %s" % (string, reversed_str))
        main_menu()

    elif (choice == 3):
        string = input("Enter string to count vowels: ")
        print("Total number of vowels:", vowel_count(string))
        main_menu()

    elif (choice == 4):
        string = input("Enter string to count number of words: ")
        print("Number of words in the string: ", word_count(string))
        main_menu()
    
    elif(choice == 5):
        exit()

    else:
        print("Invalid Choice.")
        main_menu()

main_menu()