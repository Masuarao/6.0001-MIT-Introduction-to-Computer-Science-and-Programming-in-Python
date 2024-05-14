# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORDLIST = load_words(WORDLIST_FILENAME)

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self,shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Initialise Variables for Operation
        shift_dict = {}
        lower_alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_alphabet_dict = {1:'a',2:'b',3:'c', 4:'d',5:'e',6:'f',7:'g',8:'h',
                               9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',
                               16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',
                               23:'w',24:'x',25:'y',0:'z'}
        upper_alphabet_dict = {1:'A',2:'B',3:'C', 4:'D',5:'E',6:'F',7:'G',8:'H',
                               9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',
                               16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',
                               23:'W',24:'X',25:'Y',0:'Z'}
        
        # Build shift dict
        for i in range(len(lower_alphabet_string)):
            shift_dict[lower_alphabet_string[i]] = lower_alphabet_dict[((i+shift+1)%26)]
            shift_dict[upper_alphabet_string[i]] = upper_alphabet_dict[((i+shift+1)%26)]
        
        return shift_dict
        
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        lower_alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # Build the shift dictionary
        # Loop through word and replace only letters 
        shift_dict = self.build_shift_dict(shift)
        shifted_message_list = []
            
        for i in range(len(self.message_text)):
            if (self.message_text[i] in lower_alphabet_string) or (self.message_text[i] in upper_alphabet_string):
                shifted_message_list.append(shift_dict[self.message_text[i]])
            else: 
                shifted_message_list.append(self.message_text[i])
        
        shifted_message_string = ''.join(shifted_message_list)
        return shifted_message_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Initialise tupple to return 
        best_shift = (0,self.message_text)                                      # Default return
        
        for i in range(26):                                                     # Try all 25 shifts including itself
            shifted_message = self.apply_shift(i)
            words = shifted_message.split(' ')
            real_words = 0
            for j in words:                                                     # Count the real words for each shift
                if is_word(WORDLIST, j):
                    real_words += 1
            
            if real_words > best_shift[0]:                                      # Set the tupple to return the most real words
                best_shift = (26-i,shifted_message)                         

        return best_shift
                
            
            
            
        # Break string into list by using 'space' as delimiter 
        # Use is_word(word_list, word) to count the val 
        # Get index of the highest val
        # Return lowest value and decrypted message 
if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    plain_message = PlaintextMessage('Plain test message.', 1)
    print('Encrypted message is:', plain_message.get_message_text_encrypted())
    #TODO: best shift value and unencrypted story
    test_ciphertex = CiphertextMessage("Qmbjo uftu nfttbhf.")
    print('Shift and decrypted message:',test_ciphertex.decrypt_message())
    