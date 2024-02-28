#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    return even_numbers
numbers = ([0, 1, 3, 5, 7, 8, 9])
# print (return_evens(range (10)))


def make_exclamation(sentence_list):
    make_exclamation_end = [sentence + "!" for sentence in sentence_list]
    return make_exclamation_end

sentences =(["Hello", "I'm doing great", "Python is fun"])

# print(make_exclamation(sentences))