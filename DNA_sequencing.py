import doctest

def find_longest(los: list[str]) -> str:
    """
    returns the longest string found in the given list of strings.
    If two strings have the same length, the one that was found
    first in the list (closest to the front) is returned
    >>> find_longest([])
    ''
    >>> find_longest(['AT'])
    'AT'
    >>> find_longest(['AT', 'CGA', 'TGAC', 'TGACC'])
    'TGACC'
    >>> find_longest(['GTCCA', 'ACTG', 'GAC', 'AT'])
    'GTCCA'
    >>> find_longest(['CA', 'TGCA', 'TCA', 'GTAC'])
    'TGCA'
    """
    # TODO: Complete this method
    if len(los) == 0:
        return ''
    longest_str = los[0]
    index = 0
    while index < len(los):
        if len(longest_str) < len(los[index]):
            longest_str = los[index]
        index += 1
    return longest_str
        


def get_frequency(los: list[str], to_find: str) -> int:
    """
    returns a count of the number of times to_find is found
    in the given list of strings
    >>> get_frequency([], 'AC')
    0
    >>> get_frequency(['AC', 'TAC', 'GAC', 'AC', 'GTAC'], 'AC')
    2
    >>> get_frequency(['ACTG', 'TGA', 'TTGA', 'TGGGGA', 'TGAC'], 'TGA')
    1
    >>> get_frequency(['GA', 'AAG', 'AGG', 'AGT', 'CAG'], 'AG')
    0
    >>> get_frequency(['AG', 'GA', 'AAG', 'AGG', 'AGT', 'AG', 'AG'], 'AG')
    3
    """
    # TODO: Complete this method
    count_freq = 0
    for string in los:
        if string == to_find:
            count_freq += 1
    return count_freq


def is_mutation(sequence: str) -> bool:
    """
    returns true if the given sequence contains a mutation. Any string with
    at least two of the same character in a row is considered a mutation.
    Returns True if the given string is a mutation, false otherwise.
    
    Precondition: len(sequence) >= 2 and any duplicate characters in the 
    given string will appear right beside one another.
    >>> is_mutation('ACTG')
    False
    >>> is_mutation('ACTGG')
    True
    >>> is_mutation('AACTG')
    True
    >>> is_mutation('ACCCCCTG')
    True
    >>> is_mutation('GA')
    False
    """
    # TODO: Complete this method
    mutation = False
    prev_word = 0
    next_word = 1
    while next_word < len(sequence) and mutation == False:
        if sequence[prev_word] == sequence[next_word]:
            mutation = True
        prev_word += 1
        next_word += 1
    return mutation

def break_mutation(sequence: str) -> str:
    """
    returns a string with all duplicate letters removed from sequence
    
    Any sequence with at least two of the same base in a row is 
    considered a mutation.
    
    Precondition: Any duplicate characters in the given string will
    appear right beside one another.
    >>> break_mutation('GTAC')
    'GTAC'
    >>> break_mutation('GGGTAC')
    'GTAC'
    >>> break_mutation('CGATTT')
    'CGAT'
    >>> break_mutation('AAAACC')
    'AC'
    >>> break_mutation('TTTTTTTTTTAAGGGGGGG')
    'TAG'
    """
    # TODO: Complete this method
    prev_word = 0
    next_word = 1
    new_str = ''
    length = len(sequence)
    while next_word < length:
        if sequence[prev_word] != sequence[next_word]:
            new_str += sequence[prev_word]
        prev_word += 1
        next_word += 1
    new_str += sequence[length-1]
    return new_str


def count_total_mutations(los: list[str]) -> int:
    """ 
    returns a count of the total number of strings in the given 
    list of strings that contain a mutation
    
    Any string with at least two of the same character in a row is 
    considered a mutation.
    
    Precondition: All strings have a length >= 2 and any duplicate characters 
    in a string will appear right beside one another.
    >>> count_total_mutations(['AC', 'CGT', 'TCA', 'ATG', 'GTAC', 'GA'])
    0
    >>> count_total_mutations(['ACTG', 'TGA', 'TTGA', 'TGGGGGAA', 'TGAC'])
    2
    >>> count_total_mutations(['CCAAAATT', 'GGGTT', 'AAAATTGGGCCCC',\
    'GGGTT', 'GTA'])
    4
    """
    # TODO: Complete this method
    count = 0
    for word in los:
        if is_mutation(word) == True:
            count += 1
    return count



def frequency_incl_mutations(los: list[str], to_find) -> int:
    """
    returns a count of the number of times to_find and mutations of 
    to_find are found in the given list of strings
    
    Any string with at least two of the same character in a row is 
    considered a mutation.
    
    Preconditions: All strings contain at least two characters, 
    All strings contain only characters A, C, T, or G
    Any duplicate letters within a string are beside one another
    
    >>> frequency_incl_mutations(['AC', 'TAC', 'ACG', 'AC', 'GTAC'], 'TA')
    0
    >>> frequency_incl_mutations(['AC', 'TAC', 'ACG', 'AC', 'GTAC'], 'AC')
    2
    >>> frequency_incl_mutations(['TGA', 'TTGA', 'TGGGGAA', 'TGAA'], 'TGA')
    4
    >>> frequency_incl_mutations(['TGAC', 'TGA', 'TTGA', 'TGGGGGAA',\
    'CTGA', 'TGAA'], 'TGA')
    4
    """
    # TODO: Complete this method
    count = 0
    for sequence in los:
        without_mutation_sequence = break_mutation(sequence)
        if without_mutation_sequence == to_find:
            count += 1
    return count


def create_list_from_file(file_name: str) -> list[str]:
    """
    create and return a new list containing all of the strings found
    in the file. 
    
    Precondition: there is a file with the given file_name in the same
    folder as this python file. All strings in file are all separated by a space
    >>> create_list_from_file('data0.txt')
    []
    >>> create_list_from_file('data1.txt')
    ['AC', 'TAC', 'GAC', 'AC', 'GTAC']
    """
    # TODO: Complete this method
    los = []
    file_handle = open(file_name,'r')
    for line in file_handle:
        line = line.strip()
        los = line.split(' ')
    file_handle.close()
    return los