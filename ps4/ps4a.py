# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    def letter_insertion(permutation_list,letter):
        '''
        Takes a letter and inserts into list to return all permutations 
        
        e.g. letter_insertion(['ba','ab'],'c')
        
        would return ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']

        '''
        inserted_permutation_list = []                                          # Initialise new list
        for i in permutation_list:                                              # For each member of the list
            for j in range(len(i)):                                             # insert letter to every possible positions
                inserted_permutation_list.append(i[:j]+letter+i[j:])
            inserted_permutation_list.append(i+letter)
        
        return inserted_permutation_list
        
    if len(sequence) == 1:                                                      # Base case
        return [sequence]
    else:                                                                       # Recursive case using permutation letter insert
        last_letter = sequence[-1]
        sequence = sequence[:-1]
        return letter_insertion(get_permutations(sequence),last_letter)
    
    

if __name__ == '__main__':
    
    print(get_permutations('abc'))

