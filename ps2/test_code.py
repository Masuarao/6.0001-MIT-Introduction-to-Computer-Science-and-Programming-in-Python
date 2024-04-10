# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:16:59 2024

@author: Wilson
"""
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    def narrow_search(possible_words, letter, position):
        '''
        possible_words : list of strings of possible words with same length as 
                         my_word
                letter : string of a single character to filter list of 
                         possible words
              position : position of letter in the words 
               returns : filtered possible words list
        '''
         
        
    
    possible_words = []                                                         # Create empty list to store possible words
    my_word = my_word.replace(' ','')                                           # Remove spaces
    my_word_len = len(my_word)                                                  # Store word length to reduce computation
    
    for i in wordlist:                                                          # Iterate through a shallow copy of possible words
        if len(i) == my_word_len:                                               # Append word to list if same length
            possible_words.append(i)                                            # Much less computation time vs removing elements from wordlist
            
    for i in range(len(my_word)):                                               # Looping through each letter of my_word
        if my_word[i] != '_':                                                   # Skip if letter is underscore
            for j in possible_words[:]:                                         # Iterate through all possible words 
                if j[i]!=my_word[i]:                                            # If letter at specified position does not match
                    possible_words.remove(j)                                    # Remove the letter from the list
                                                                                # Much less elements - reasonable to use remove function
    
    if not possible_words:                                                      # If empty list print no matches
        print('No matches found')
    else:                                                                       # Else print list
    
        print(' '.join(possible_words))
        
show_possible_matches("a_ pl_ ")