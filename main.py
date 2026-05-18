# Programmers: Lamar Holloway and mcallister
# Course: Intro to computer science
# Due Date: 4/14/2026
# Lab Assignment: Lab 10
# Problem Statement: tranlate the morse code to english base on inputed file
# Data In: The user's file they want to uses
# Data Out: morse in english line by line

# Name: validate_file
# Purpose: Validate the file name input
# Parameters: N/A
# Return: user_file
def validate_file():
    valid_files = ["morse1.txt", "morse2.txt", "morse3.txt"]

    input_file = input("Options:\n(morse1.txt)\n(morse2.txt)\n(morse3.txt)\nPlease enter the name of the file you want to choose: ")

    while input_file not in valid_files:
        print("Invalid file. Please choose from the list.")
        input_file = input("(morse1.txt)\n(morse2.txt)\n(morse3.txt)\nPlease enter the name of the file: ")

    return input_file

# Name: store_conversion
# Purpose: Store conversion information into a dictionary (file name is morsecode.txt)
# Parameters: morsecode.txt
# Return: morse_dict
def store_conversion(file_name):
    morse_dict = {}

    file = open(file_name, 'r')

    for line in file:
        parts = line.strip().split()

        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            morse_dict[value] = key

    file.close()

    return morse_dict
# Name: read_morse_text
# Purpose: Read in the morse code text file
# Parameters: user_file
# Return: user_file_list
def read_morse_text(user_file):
    user_file_list = []

    file = open(user_file, 'r')

    for line in file:
        user_file_list.append(line.strip())

    file.close()

    return user_file_list
# Name: morse_to_english
# Purpose: Converting the morse code file to an english file
# Parameters: user_file, morse_dict
# Return: english_file
def morse_to_english(user_file_list, morse_dict, output_file):
    out_file = open(output_file, 'w')

    for line in user_file_list:
        words = line.split()
        sentence = ""

        for code in words:
            if code in morse_dict:
                sentence += morse_dict[code]
            else:
                sentence += '?'  # unknown symbol safety

        print(sentence)

    out_file.close()

# Name: main
# Purpose: call previous functions
# Parameters:
# Return:
def main():

    print("Morse Code to English Converter")

    conversion_file = "morsecode.txt"
    input_file = validate_file()


    # Process files
    morse_dict = store_conversion(conversion_file)
    user_file_list = read_morse_text(input_file)

    # Convert and write output
    morse_to_english(user_file_list, morse_dict, "morse.txt")

    print("Conversion complete! Check your output file.")

main()
