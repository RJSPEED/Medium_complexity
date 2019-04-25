"""LOGICAL APPROACH:
1. Create fx that takes a str and remove non-word chars, and stores in a list
2. Create a subsequent fx that takes the words in the list and pops a dict
   with word and related count
3. Create a sorted list of the words, sorted by count DESC
4. Print the top n no. of word and their counts, n supplied by fx input
"""
import re
import json
import collections
import operator

def string_format(input_string):
        #Use re.sub to identify all chars that are not in range a-z or A-Z
        #and then replace with a blank space, arguments = match pattern, replace
        #string, search string. Used casefold to remove capitalisation.
        return re.sub("[^a-zA-Z]","", input_string).casefold().strip()

def word_count(filename, word_range):
    word_count_dict = {}
    text_list =[]
    formatted_list =[]
    with open(filename, 'r') as file_object:
        #Read entire file
        whole_text = file_object.read()
        #Add items split by blank space into list
        text_list = whole_text.split()
        #Next loop through list elements, feeding values into string_format fx
        #that removes none word chars and return the formatted value. Populate 
        #another list with formatted values. 
        for i in text_list:
                formatted_list.append(string_format(i))
        #Use collections.counter to pop a dict of the unique words and their 
        #counts.
        #INFO: A Counter is a dict subclass for counting hashable objects. It's
        #an unordered collection where elements are stored as dictionary keys
        #and their counts are stored as dictionary values. Counts are allowed
        #to be any integer value including zero or negative counts.
        counted_dict=collections.Counter(formatted_list)
        #Create sorted list of dict items
        sorted_list = sorted(counted_dict.items(), key=operator.itemgetter(1), reverse=True)
        #Print top n number from list
        for i in range(0,word_range):
            print(sorted_list[i])

word_count("article.txt",5)
