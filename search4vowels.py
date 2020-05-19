def search4vowels(phrase:str) -> set:
    '''Возвращает гласные в фразе'''
    vowels = set('aeiou')
    phrase = input("Provide a word to search for vowels: ")
    return vowels.intersection(set(phrase))

print (search4vowels(input()))