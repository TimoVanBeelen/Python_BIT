# Python file containing all the intermediate level exercises from BIT module 1
# Course code: 202001061
# Author: Timo van Beelen & Alfonso Capitano
# Date: 2023/09/11

from collections import defaultdict
from pprint import pprint


# Exercise 1: calculate the average value of a key in a dictionary. The values for a certain key are given in a list
# Input: A dictionary with a key and a list of values (type: list with float)
# Output: A dictionary with a key and the average of the list as value (type: float)
def calculate_average_price(products_dict :dict):
    for item in products_dict:
        total_of_values = 0           
        for value in products_dict[item]:
            # Validate the entries of the list
            if type(value) != float: 
                print('Invalid argument. Expected a float, got a %s instead' %(type(value)))
                return None

            # If entry is valid, add it to the total
            total_of_values += value

        # Take the average of the total
        products_dict[item] = round(total_of_values/len(products_dict[item]), 2)

    return products_dict


# Exercise 2: Take in a text and count the amount a word occurs in the text, except stop words. It should be case insensitive
# Input: text (type str) with words and a list of stop words
# Output: A dictionary with as key the word and as value the amount of occurences
def count_word_occurences(text :str, stop_words :list):
    # Validation
    if not isinstance(text, str) or len(text) == 0 or len(stop_words) == 0:
        print('Invalid input')
        return None
    for words in stop_words:
        if not isinstance(words, str):
            print('Invalid input')
            return None

    occurence_dict = defaultdict(int)
    text = text.replace('.', '')
    list_of_words = text.split(' ')
    for word in list_of_words:
        # If the word is in the list of stop words, continue to the next instance
        if word.lower() in stop_words:
            continue
        occurence_dict[word] += 1

    return occurence_dict


# Exercise 3: The function takes an ordered list of items of any type and uses the binary search algorithm to search for the item specified in the argument.
#             If the searched item is found, then the function returns its index in the list. Otherwise it returns -1
# Input: An ordered list and an item to search (type: any)
# Output: The index of the item in the list or -1 for when it is not found
def binary_search(ordered_list :list, item_to_search):
    # Validation
    if len(ordered_list) == 0:
        print('Invalid Argument: ordered_list must be non-empty')
        return None
    for item in ordered_list:
        if type(item) is not type(ordered_list[0]):
            print('Type Mismatch: not all items of `ordered_list` have the same type of `item_to_search`')
            return None
    
    # React to the catch statement that the first element cannot be reached
    if ordered_list[0] is item_to_search: return 0

    # Assume to search through the entire list
    low_bound = 0
    high_bound = len(ordered_list)
    last_middle = 0
    while low_bound<high_bound-1:
        middle = (low_bound+high_bound)//2

        if ordered_list[middle] is item_to_search:
            return middle   # Middle is the index of the item in the list

        # Otherwise adapt the low or high bound of the search
        if ordered_list[middle] < item_to_search:
            low_bound = middle
        else:
            high_bound = middle
    
    return -1 # Return -1 when the item is not found


# Exercise 4: Takes a dictionary with as key a string representing the name of a city and as value a list of tempratures as floats observed in the respective city over a period of time. The function should calculate the amplitude of temperature variation and return a dict with as key the city name and as value the amplitude (max difference) between temperatures in 1 digit decimals
def amplitude_temperature(cities_temperature :dict):
    # Validation
    if len(cities_temperature) == 0: 
        print('Invalid argument. Check specifications.')
        return None
    for key in cities_temperature:
        if not isinstance(key, str) and len(cities_temperature[key]) == 0:
            print('Invalid argument. Check specifications.')
            return None
        for value in cities_temperature[key]:
            if not isinstance(value, float):
                print('Invalid argument. Check specifications.')
                return None

    


# Main script, add test functions here
if __name__ == "__main__":
    pasta_al_salmone ={
        "Pomodorini/Tomatten/Tomatoes 250g pack": [1.99, 2.49, 1.19, 1.99],
        "Capperi/Kappertjes/Capers": [0.69, 0.79, 0.89, 0.69],
        "Olive oil extra virgin 750ml": [6.59, 7.29, 5.99, 6.39],
        "Prezzemolo/Peterselie/Parsley": [0.99, 0.89, 0.99, 0.99],
        "Coriandolo/Koriander/Coriander": [0.99, 0.89, 0.89, 0.89],
        "Pasta Rummo 500g (Conchiglioni Rigati)": [2.29, 2.99, 2.99, 2.09],
        "Salmone/Zalm/Salmon 250g": [4.99, 4.99, 4.99, 4.99],
        "Aglio/Knoflook/Garlic": [0.99, 0.89, 0.99, 1.09],
        "Olive/Olijven/Olives (Taggiasche)": [2.79, 3.49, 2.99, 3.09],
        "Vino Bianco/Wit Wijn/White Wine (Greco di Tufo)": [14.95, 13.99, 14.18, 16.69],
        "Caffe Lavazza (Black) 250g": [2.79, 3.09, 3.39, 2.79]
    }
    pprint(calculate_average_price(pasta_al_salmone))

    text = "This is a sample text. This text contains sample words."
    stop_words = ["is", "a", "this"]

    print(count_word_occurences(text=text, stop_words=stop_words))

    dataset = [
        "almond",
        "apple",
        "apricot",
        "banana",
        "blueberry",
        "cantaloupe",
        "cherry",
        "coconut",
        "cranberry",
        "date",
        "dragonfruit",
        "elderberry",
        "fig",
        "grape",
        "grapefruit",
        "guava",
        "honeydew",
        "kiwi",
        "lemon",
        "lime",
        "mango",
        "nectarine",
        "orange",
        "papaya",
        "peach",
        "pear",
        "pineapple",
        "plum",
        "pomegranate",
        "quince",
        "raspberry",
        "strawberry",
        "tomato",
        "watermelon",
        # ... Add more words here ...
        "zebra"
    ]


    print(binary_search(dataset, 'tomato'))
