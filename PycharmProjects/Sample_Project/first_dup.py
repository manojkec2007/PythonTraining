"""
Python module for finding the first duplicate character in a string

"""
__author__ = "Manoj K V"

# -*- coding: utf-8 -*-


def character_count_string(word):
    array_list = []  # Create Empty List and later append
    for char in word:
        cnt = word.lower().count(char.lower())
        array_list.append({"char": char, "count": cnt})
    return array_list


def first_repeat_char(word):
    """
    This function will return the
    first Repeated Character in the input string
    """
    array_list = character_count_string(word)
    for item in array_list:
        if item["count"] > 1:
            print "First Duplicate Character Found"
            return item["char"]
        else:
            return "No Duplicate Character Found"

if __name__ == '__main__':
    # Get the input from the User
    input_str = raw_input("Enter the input :")
    print input_str

    # Calling character_count_string function
    output = character_count_string(input_str)
    print "Each Character and it's No.of Occurrences in the input string as belows:"
    for out in output:
        print out

    # Calling first_repeat_char function
    first_repeat_chr_output = first_repeat_char(input_str)
    print "First Repeated Character in the input string is:", first_repeat_chr_output
