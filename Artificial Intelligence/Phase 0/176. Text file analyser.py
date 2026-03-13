import os


# ================= FILE PATH =================

def get_file_path():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    folder_path = os.path.join(base_dir, "other_files")

    file_name = input("Enter text file name: ")

    return os.path.join(folder_path, file_name)


# ================= READ FILE =================

def read_file(file_path):

    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content

    except FileNotFoundError:
        print("File not found.")
        return None


# ================= COUNT LINES =================

def count_lines(text):

    lines = text.split("\n")
    print("Total Lines:", len(lines))


# ================= COUNT WORDS =================

def count_words(text):

    words = text.split()
    print("Total Words:", len(words))


# ================= COUNT CHARACTERS =================

def count_characters(text):

    print("Total Characters:", len(text))


# ================= WORD FREQUENCY =================

def word_frequency(text):

    words = text.lower().split()

    freq = {}

    for word in words:

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print("\nWord Frequency:")
    for word, count in freq.items():
        print(word, ":", count)

    return freq


# ================= MOST FREQUENT WORD =================

def most_frequent_word(freq):

    if not freq:
        return

    word = max(freq, key=freq.get)

    print("\nMost Frequent Word:", word)
    print("Frequency:", freq[word])


# ================= ANALYZE FILE =================

def analyze_file():

    path = get_file_path()

    text = read_file(path)

    if text is None:
        return

    count_lines(text)
    count_words(text)
    count_characters(text)

    freq = word_frequency(text)

    most_frequent_word(freq)


# ================= MAIN MENU =================

def main_menu():

    while True:

        print("\n====== TEXT FILE ANALYZER ======")
        print("1. Analyze Text File")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyze_file()

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()