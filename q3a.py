# Write a Python program that accepts a sentence and find the number of words, digits, uppercase letters and lowercase letters.

def manipulate(msg):
    print('word count: '+ str(len(msg.split())))
    digit_count = 0
    upper_count = 0
    lower_count = 0
    for letter in msg:
        if letter.isdigit():
            digit_count += 1
        elif letter.isalpha():
            if letter.islower():
                lower_count += 1
            else:
                upper_count += 1
    print('Uppercase count: '+str(upper_count))
    print('Lowercase count: '+str(lower_count))
    print('Digit count: '+str(digit_count))


sentence = input('Enter a sentence: ')

manipulate(sentence)