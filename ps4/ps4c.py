# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import sys
from ps4a import get_permutations
from ps4b import is_word

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORDLIST = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = WORDLIST
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        lower_consonants_string = 'bcdfghjklmnpqrstvwxyz'
        upper_consonants_string = 'BCDFGHJKLMNPQRSTVWXYZ'
        lower_vowel_string = 'aeiou'
        upper_vowel_string = 'AEIOU'
        transpose_dictionary_map = {}
        
        def check_vowels(input_string):
            '''
            Checks if input_string argument is a string containing vowels
            
            1. Checks if argument is a string 
            
            2. Checks if argument is 5 characters long 
            
            3. Checks if argument contains all 5 vowels to be mapped
            
            returns boolean

            '''
            if not isinstance(input_string, str):                               # Check if input is a string
                return False
            
            if len(input_string) !=5:                                           # Check that there is only 5 letters
                return False
            
            vowels = "aeiou"                                                    # Check for vowels appearing exactly once
            vowel_count = {vowel: 0 for vowel in vowels}                        

            for char in input_string:
                if char in vowels:
                    vowel_count[char] += 1
                    
            all_vowels_once = all(count == 1 for count in vowel_count.values())

            return all_vowels_once
        
        if check_vowels(vowels_permutation):
            
            for i in range(len(lower_consonants_string)):                       # Map consonants
                transpose_dictionary_map[lower_consonants_string[i]] = lower_consonants_string[i]
                transpose_dictionary_map[upper_consonants_string[i]] = upper_consonants_string[i]
                
            for i in range(len(lower_vowel_string)):                            # Map Vowels
                transpose_dictionary_map[lower_vowel_string[i]] = vowels_permutation[i]
                transpose_dictionary_map[upper_vowel_string[i]] = vowels_permutation[i].upper()
            
            return transpose_dictionary_map
                
        else:
            print('Error in input for function build_transpose_dict in SubMessage',
                  'class, please debug.')
            sys.exit()            
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        # input is text and dictionary
        # ACcording to dictionary return encrypted text 
        
        lower_alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Build the shift dictionary
        # Loop through word and replace only letters 
        shifted_message_list = []
            
        for i in range(len(self.message_text)):
            if (self.message_text[i] in lower_alphabet_string) or (self.message_text[i] in upper_alphabet_string):
                shifted_message_list.append(transpose_dict[self.message_text[i]])
            else: 
                shifted_message_list.append(self.message_text[i])
        
        shifted_message_string = ''.join(shifted_message_list)
        return shifted_message_string
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = WORDLIST
        
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowel_perms = get_permutations('aeiou')                                 # Initialise list for vowel perms
        valid_count = 0                                                         # Initialise tracking variables 
        valid_message = self.message_text
        lower_vowel_string = 'aeiou'
        upper_vowel_string = 'AEIOU'
        
        for i in vowel_perms:                                                   # Check all perms
            decrypt_dict = self.build_transpose_dict(i)
            # modify the dictionary to do the reverse
            #for j in range(len(i)):
                #decrypt_dict[i[j]] = lower_vowel_string[j]
                #decrypt_dict[i[j].upper()] = lower_vowel_string[j].upper()
                
                
            
            decrypted_message = self.apply_transpose(decrypt_dict)
            words = decrypted_message.split(' ')
            
            count_real_words = 0
            
            for j in words:                                                     # Count the real words for each shift
                if is_word(WORDLIST, j):
                    count_real_words += 1
            
            if count_real_words > valid_count:
                valid_message = decrypted_message
                valid_count = count_real_words
                
        return valid_message
            
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Can we get much higher, so high.")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
     
    #TODO: WRITE YOUR TEST CASES HERE
