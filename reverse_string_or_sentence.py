test_string_sentence = 'how the **** do you reverse a string, innit?'

def string_reverser(string):
    reversed_string = string[::-1]

    return reversed_string

def sentence_reverser(sentence):
    words_list = sentence.split()
    reversed_list = words_list[::-1]
    reversed_sentence = " ".join(reversed_list)

    return reversed_sentence

example_1 = string_reverser(test_string_sentence)
print(example_1)

example_2 = sentence_reverser(test_string_sentence)
print(example_2)
