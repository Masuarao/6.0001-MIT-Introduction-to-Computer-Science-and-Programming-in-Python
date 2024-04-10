# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:                                                       
        if not(i in letters_guessed):                                           # If there is a letter missing 
            return False                                                        # return false
    return True  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    unique_letters = set(letters_guessed)                                       # Remove duplicates by creating a set 
    correct_letters_list = ['_ ']*len(secret_word)                              # Use mutable list made of '_ '
    
    for i in unique_letters:                                                    # Loop through unique letters in secret word
        for j in range(len(secret_word)):
            if i == secret_word[j]:                                             # Compare index by index with guessed word
                correct_letters_list[j] = i                                     # Replace at index if same letter
    
    correct_letters_string = ''.join(correct_letters_list)                      # Convert guessed word list to string  
                    
    return correct_letters_string                                               # Return guessed word string 
    
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # Create an alphabet array
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z']
    letters_guessed_set = set(letters_guessed)                                  # Eliminate duplicates in letters guessed by converting to set
    
    for i in letters_guessed_set:                                               # Remove valid letters guessed from alphabet
        for j in alphabet:
            if i == j :
                alphabet.remove(j)
    
    letters_guessed_string = str(''.join(alphabet))                             # Assign remaining letters to a string variable
    return letters_guessed_string                                               # Return remaining letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    def penalty(warnings, guesses_left, secret_word, letters_guessed, guessed_letter):
        '''
        Function for handling penalty
        Prints error message
        Computes remaining warnings and guesses
        
        '''
        if warnings == 0:                                                       # 1. Reduce 1 guess with warnings left
            guesses_left -= 1                                                   
            if guessed_letter.isalpha():                                        # 1.1 Alphabetical letter
                print('Oops! You'+"'"+
                      've already guessed that letter. You have no warnings left. You have',
                      guesses_left,'guesses left:', 
                      get_guessed_word(secret_word, letters_guessed))
            else:                                                               # 1.2 Non-alphabetical letter 
                print('Oops! That is not a valid letter. You have no warnings left. You have',
                      guesses_left,'guesses left:', get_guessed_word(secret_word, letters_guessed))
                
        else:                                                                   # 2: Reduce 1 warning with warnings left  
            warnings -= 1
            if guessed_letter.isalpha():                                        # 2.1: Alphabetical letter
                print('Oops! You'+"'"+'ve already guessed that letter. You have', warnings ,
                      'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:                                                               # 2.2: Non-alphabetical letter
                print('Oops! That is not a valid letter. You have', warnings ,
                     'warnings left:', get_guessed_word(secret_word, letters_guessed))
        return [warnings, guesses_left]                                         # Return list of warnings and guesses
        
    def play_hangman(guesses_left,warnings, letters_guessed,secret_word):
        '''
        Iterates one cycle of the game and returns:
            1. Guesses left 
            2. Warnings
            3. Guessed letters
        '''
        print("You have",guesses_left,"guesses left.")                          # Remind user on guesses left
        print("Available letters:", get_available_letters(guessed_letters))     # Remind user on unguessed letters
        guessed_letter = input("Please guess a letter: ")                       # Request user to guess ONE letter
        guessed_letter = str(guessed_letter)                                    # Store guess in a string
        
        # Game branch
        if guessed_letter.isalpha():                                            # 1. Input is a letter              
            guessed_letter = guessed_letter.lower()                             # Set letter to lower case
            if guessed_letter in letters_guessed:                               # 1.1 Letter already guessed - penalty
                [warnings,guesses] = penalty(warnings, guesses_left, 
                                             secret_word, letters_guessed, 
                                             guessed_letter)
            else:                                                               # 1.2 Letter not guessed                                
                letters_guessed.add(guessed_letter)                             # Add letter to guessed letters
                if guessed_letter in secret_word:                               # 1.2.1 Letter is in secret word   
                    print('Good guess:', 
                          get_guessed_word(secret_word, letters_guessed))       # Congratulate player
                else:                                                           # 1.2.2 Letter not in secret word                          
                    print('Oops! That letter is not in my word:', 
                          get_guessed_word(secret_word, letters_guessed))
                    if guessed_letter in ['a','e','i','o','u']:                 # 1.2.2.1 Letter is a vowel
                        guesses_left -= 2                                       # Subtract two guesses  
                    else:                                                       # 1.2.2.1 Letter is a consonant 
                        guesses_left -=1                                        # Subtract one guess
        else:                                                                   # 2. Input is not a letter
            [warnings,guesses] = penalty(warnings, guesses_left, secret_word, 
                                         letters_guessed,guessed_letter)        # Call warning function
        print("-------------")                                                  # Print separator at the end of iteration
        return [guesses_left,warnings]                                          # Return list of warnings and guesses

    # Function that initialises the game 
    def initialise_hangman(secret_word,guesses_left):
        '''
        Print initialisation message
        '''
        print("Welcome to the game Hangman!")
        print("I am thinking of a word that is",len(secret_word), "letters long.")
        print("-------------")
                                                                                # START OF HANGMAN FUNCTION
                                                                                # Initislisation
    guesses_left = 6                                                           # Initialise initialise guesses
    warnings = 3                                                                # Initialise initialise warnings
    guessed_letters = set()                                                     # Initialise guessed letters set
    initialise_hangman(secret_word,guesses_left)                                # Print starting messages
    
    while guesses_left > 0:                                                     # Keep playing the game until no guesses left
        [guesses_left,warnings] = play_hangman(guesses_left, warnings ,
                                               guessed_letters, secret_word)
        if is_word_guessed(secret_word, guessed_letters):                       # Break if whole word is revealed
            break
                                                                                # Game termination
    if guesses_left > 0:                                                        # Lose game
        score = guesses_left*len(set(secret_word))
        print('Congratulations, you won!')
        print('Your total score for this game is:', score)
    else:                                                                       # Win game
        print('Sorry, you ran out of guesses. The word was', secret_word)
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')                                           # Remove spaces
    
    for i in range(len(my_word)):                                               # Compare letters
        if not(my_word[i] == other_word[i] or my_word[i] == '_'):               # False if not same letters or not a underscore
            return False
        elif my_word[i] == '_':                                                 # If it is a underscore
            if(other_word[i] in my_word):                                       # Return false if corresponding letter is already guessed
                return False
    return True 




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

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
        

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    def penalty(warnings, guesses_left, secret_word, letters_guessed, guessed_letter):
        '''
        Function for handling penalty
        Prints error message
        Computes remaining warnings and guesses
        
        '''
        if warnings == 0:                                                       # 1. Reduce 1 guess with warnings left
            guesses_left -= 1                                                   
            if guessed_letter.isalpha():                                        # 1.1 Alphabetical letter
                print('Oops! You'+"'"+
                      've already guessed that letter. You have no warnings left. You have',
                      guesses_left,'guesses left:', 
                      get_guessed_word(secret_word, letters_guessed))
            else:                                                               # 1.2 Non-alphabetical letter 
                print('Oops! That is not a valid letter. You have no warnings left. You have',
                      guesses_left,'guesses left:', get_guessed_word(secret_word, letters_guessed))
                
        else:                                                                   # 2: Reduce 1 warning with warnings left  
            warnings -= 1
            if guessed_letter.isalpha():                                        # 2.1: Alphabetical letter
                print('Oops! You'+"'"+'ve already guessed that letter. You have', warnings ,
                      'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:                                                               # 2.2: Non-alphabetical letter
                print('Oops! That is not a valid letter. You have', warnings ,
                     'warnings left:', get_guessed_word(secret_word, letters_guessed))
        return [warnings, guesses_left]                                         # Return list of warnings and guesses
        
    def play_hangman(guesses_left,warnings, letters_guessed,secret_word):
        '''
        Iterates one cycle of the game and returns:
            1. Guesses left 
            2. Warnings
            3. Guessed letters
        '''
        print("You have",guesses_left,"guesses left.")                          # Remind user on guesses left
        print("Available letters:", get_available_letters(guessed_letters))     # Remind user on unguessed letters
        guessed_letter = input("Please guess a letter: ")                       # Request user to guess ONE letter
        guessed_letter = str(guessed_letter)                                    # Store guess in a string
        
        # Game branch
        if guessed_letter.isalpha():                                            # 1. Input is a letter              
            guessed_letter = guessed_letter.lower()                             # Set letter to lower case
            if guessed_letter in letters_guessed:                               # 1.1 Letter already guessed - penalty
                [warnings,guesses] = penalty(warnings, guesses_left, 
                                             secret_word, letters_guessed, 
                                             guessed_letter)
            else:                                                               # 1.2 Letter not guessed                                
                letters_guessed.add(guessed_letter)                             # Add letter to guessed letters
                if guessed_letter in secret_word:                               # 1.2.1 Letter is in secret word   
                    print('Good guess:', 
                          get_guessed_word(secret_word, letters_guessed))       # Congratulate player
                else:                                                           # 1.2.2 Letter not in secret word                          
                    print('Oops! That letter is not in my word:', 
                          get_guessed_word(secret_word, letters_guessed))
                    if guessed_letter in ['a','e','i','o','u']:                 # 1.2.2.1 Letter is a vowel
                        guesses_left -= 2                                       # Subtract two guesses  
                    else:                                                       # 1.2.2.1 Letter is a consonant 
                        guesses_left -=1                                        # Subtract one guess
        else:                                                                   # 2. Input is not a letter
            if guessed_letter == '*':                                           # 2.1 Input is '*' display hint
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:                                                               # Penalty
                [warnings,guesses] = penalty(warnings, guesses_left, 
                                             secret_word, letters_guessed,
                                             guessed_letter)                    # Call warning function
        print("-------------")                                                  # Print separator at the end of iteration
        return [guesses_left,warnings]                                          # Return list of warnings and guesses

    # Function that initialises the game 
    def initialise_hangman(secret_word,guesses_left):
        '''
        Print initialisation message
        '''
        print("Welcome to the game Hangman!")
        print("I am thinking of a word that is",len(secret_word), "letters long.")
        print("-------------")
                                                                                # START OF HANGMAN FUNCTION
                                                                                # Initislisation
    guesses_left = 6                                                           # Initialise initialise guesses
    warnings = 3                                                                # Initialise initialise warnings
    guessed_letters = set()                                                     # Initialise guessed letters set
    initialise_hangman(secret_word,guesses_left)                                # Print starting messages
    
    while guesses_left > 0:                                                     # Keep playing the game until no guesses left
        [guesses_left,warnings] = play_hangman(guesses_left, warnings ,
                                               guessed_letters, secret_word)
        if is_word_guessed(secret_word, guessed_letters):                       # Break if whole word is revealed
            break
                                                                                # Game termination
    if guesses_left > 0:                                                        # Lose game
        score = guesses_left*len(set(secret_word))
        print('Congratulations, you won!')
        print('Your total score for this game is:', score)
    else:                                                                       # Win game
        print('Sorry, you ran out of guesses. The word was', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
