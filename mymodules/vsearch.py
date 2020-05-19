def search4vowels(phrase:str) -> set:
    '''Возвращает гласные в фразе'''
    vowels = set('aeiou')
    #phrase = input("Provide a word to search for vowels: ")
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """находит заданные буквы в фразе"""
    return set(letters).intersection(set(phrase))

#print (search4letters('debug'))