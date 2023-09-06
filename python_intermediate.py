# Python file containing all the intermediate level exercises from BIT module 1
# Course code:
# Author: Timo van Beelen
# Date: 2023/09/06

# Exercise 1: Month name by its number using dictionairies
# Input: The number of the month (as an integer)
# Output: The name of the month
def month_name_alt(month_number :int):
    # Check if the input is correct
    if type(month_number) != int or month_number > 12 or month_number < 1:
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


# Main script, call the file directly and this is run
if __name__ == "__main__":
    for i in range(1, 13):
        print(month_name_alt(i))

    items_list = ["Hey", "there", "I", "did", "not", "see", "you", "there!", 
                  "Let", "me", "tell", "ya", "a", "secret:", 93, "'vo"]
    print(linear_search(items_list, 93))


