# Python file containing all the intermediate level exercises from BIT module 1
# Course code: 202001061
# Author: Timo van Beelen & Alfonso Capitano
# Date: 2023/09/11

# Exercise 1: Month name by its number using dictionairies
# Input: The number of the month (as an integer)
# Output: The name of the month
def month_name_alt(month_number :int):
    # Check if the input is correct
    if type(month_number) is not int or month_number > 12 or month_number < 1:
        return ValueError('Invalid input')

    # Define the dictionairy, linking the names to its number
    month_dictionairy = {1: 'January',
                         2: 'February',
                         3:'March',
                         4:'April',
                         5:'May',
                         6:'June',
                         7:'July', 
                         8:'August', 
                         9:'September',
                         10:'October', 
                         11:'November', 
                         12:'December'}
    return month_dictionairy.get(month_number) # We could also add the 'Invalid input' as second argument to return when a key is given that is not linked to the dict. However, raising an error is cleaner for future variable handling


# Exercise 2: Search a list linearly for an item
# Inputs: A list of items (type: list) and the item to be found (no type specified)
# Output: The index of the item in the list (type: integer)
def linear_search(list_of_items :list, item):
    # When the list is empty, return -2
    if len(list_of_items) == 0: 
        return -2
    
    # If the item is in the list, return its index. Otherwise return -1
    if item in list_of_items:
        return list_of_items.index(item)
    else: 
        return -1


# Exercise 5: Remove duplicates from a list of names
# Input: An unordened list (type: list) containing string elements
# Output: A list (type: list) with the same strings but with duplicates removed
def remove_duplicates(list_of_names :list):
    # Check validity of input
    if len(list_of_names) < 2:
        print('Invalid argument: list_of_names must contain only string (len >= 2)')
        return None
    for item in list_of_names:
        if not isinstance(item, str):
            print('Invalid argument: list_of_names must contain only string (len >= 2).')
            return None
    
    duplicateless_list = []
    for item in list_of_names:
        if item not in duplicateless_list:
            duplicateless_list.append(item)

    return duplicateless_list


# Exercise 8: Return a tuple with the word with the least vowels from a list of words and how many vowels that word has
# Input: A list (type: list) of words (type: string)
# Output: A tuple containing the word (type: string) and the amount of vowels (type integer)
def get_least_vowels_word(list_of_words):
    # Check the validity of the input
    if len(list_of_words) < 2:
        print('Invalid Argument. List length must be >= 2, only strings allowed.')
        return None
    for item in list_of_words:
        if not isinstance(item, str):
            print('Invalid Argument. List length must be >= 2, only strings allowed.')
            return None
    
    
    word_with_least_vowels = list_of_words[0] # Set the word with the least vowels to the first of the list to start
    least_vowels_amount = 10
    for word in list_of_words:
        vowels_amount = 0
        for char in ['A', 'E', 'Y', 'U', 'I', 'O', 'a', 'e', 'y', 'u', 'i', 'o']:   #"AEYUIOaeyuio"
            vowels_amount += word.count(char)
        
        # Check if the count is lower than the lowest to that point and change accordingly
        if vowels_amount < least_vowels_amount:
            least_vowels_amount = vowels_amount
            word_with_least_vowels = word

    return (word_with_least_vowels, least_vowels_amount)
                

# Exercise 9: Capitalize the first letter of each word in a sentence
# Input: A string
# Output: The same string with each word starting with a capital letter
def capitalize_words(sentence :str):
    # Check validity of the input
    if not isinstance(sentence, str) or len(sentence) < 1:
        print('Invalid Argument. It must be a non-empty string.')
        return None

    return sentence.title()


# Main script, call the file directly and this is run
if __name__ == "__main__":
    for i in range(1, 13):
        print(month_name_alt(i))

    items_list = ["Hey", "there", "I", "did", "not", "see", "you", "there", "!", 
                  "Let", "me", "tell", "you", "a", "secret:", 93, "'vo"]
    print(linear_search(items_list, 93))
    
    items_list.remove(93)
    print(remove_duplicates(["there", "are", "are", "are", "duplicates", "here", "and", "there"]))
    print(get_least_vowels_word(items_list))



