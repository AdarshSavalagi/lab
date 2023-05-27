import difflib


def similarity_checker(first_string, second_string):
    result = difflib.SequenceMatcher(a=first_string.lower(), b=second_string.lower())
    return result.ratio()


first_string = input('Enter first string: ')
second_string = input('Enter second string: ')

print('Similarity between two said strings: ' + str(similarity_checker(first_string, second_string)))
