# Python file containing all the intermediate level exercises from BIT module 1
# Course code:
# Author: Timo van Beelen
# Date: 2023/09/06

# Exercise 1: Month name by its number using dictionairies
# Input: The number of the month (as an integer)
# Output: The name of the month
def month_name_alt(month_number :int):
    if type(month_number) != int or month_number > 12 or month_number < 1:
        return ValueError('Invalid input')
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
    return month_dictionairy.get(month_number)


# Main script, call the file directly and this is run
if __name__ == "__main__":
    for i in range(1, 12):
        print(month_name_alt(i))

