def display_first_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        for i, line in enumerate(file, start=1):
            print(line.rstrip())
            if i == n:
                break

def find_word_frequency(file_name, word):
    frequency = 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for w in words:
                if w == word:
                    frequency += 1
    return frequency


file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to display: "))
word_to_find = input("Enter the word to find: ")

print("First", n, "lines of the file:")
display_first_n_lines(file_name, n)

frequency = find_word_frequency(file_name, word_to_find)
print("Frequency of word", word_to_find, "in the file:", frequency)
