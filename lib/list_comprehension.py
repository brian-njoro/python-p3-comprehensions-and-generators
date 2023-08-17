#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if (n%2 == 0) == True]
    return even_list

def make_exclamation(sentence_list):
    exclamation_list = [sentence.strip() + '!' for sentence in sentence_list]
    return exclamation_list