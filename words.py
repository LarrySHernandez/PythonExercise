def print_upper_words(list, letters):
    """This function allows us to take any string input and provide an output with 
    all the letters in uppercase"""

    # this should print the string, starting with the letter e, all in uppercase
    for word in list: 
        upper_case_string = ""
        for letter in letters:       
            if word[0].capitalize() == letter.capitalize():
                for char in word:
                    upper_case_string += char.capitalize() 
        print(upper_case_string, end= "\n")


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])