# program for counting words in a file

#---# Guide Lines pt 1:
# Run the program in command line
# ! Say what working directory currently is
# ! List all files / folders in directory
#---#

from pathlib import Path
import os
cwd = os.getcwd()
listd = os.listdir()

print("----------------------------")
print("Welcome to Word Counter 1.0!")
print("----------------------------")

# Working directory currently in
print("")
print("----------------------------")
working_directory_question = input("Do you want to know what your working directory is? (y or n): ")
print("----------------------------")
print("")

if working_directory_question == "y":
    print("")
    print("----------------------------")
    print(f"here is the current working directory ---> " + cwd )
    print("----------------------------")
    print("")
elif working_directory_question == "n":
    print("")
    print("----------------------------")
    print("ok, sending forward")
    print("----------------------------")
    print("")
else:
    print("")
    print("----------------------------")
    input ("did not input either y or n, last chance to get the working directory. (y or n): ")
    print("----------------------------")
    print("")
    if working_directory_question == "y":
        print("")
        print("----------------------------")
        print("here is the current working directory --->  " + cwd )
        print("----------------------------")
        print("")
    else:
        print("")
        print("----------------------------")
        print("ok, sending forward")
        print("----------------------------")
        print("")


# List all files and folders in directory
print("")
print("----------------------------") 
files_folders_questions = input("Do you want to know what files and folders are in this directory? (y or n): " )
print("----------------------------")
print("")

if files_folders_questions == "y":
    print("")
    print("----------------------------")
    print("here are the files and folders:  ") 
    print(listd)
    print("----------------------------")
    print("")
elif files_folders_questions == "n":
    print("")
    print("----------------------------")
    print("ok, sending forward")
    print("----------------------------")
    print("")
else:
    print("")
    print("----------------------------")
    input ("did not input either y or n, last chance to get the working directory. (y or n): ")
    print("----------------------------")
    print("")
    if files_folders_questions == "y":
        print("")
        print("----------------------------")
        print("here are the current files and folders in the directory:  ")
        print(listd)
        print("----------------------------")
        print("")
    else:
        print("")
        print("----------------------------")
        print("ok, sending forward")
        print("----------------------------")
        print("")


#---# Guide Lines pt 2:
# Run the program in command line
# ! Ask what file
# ! Open the relative path of the selected file
# ! The relative path to the three files is as follows:
    # ./monty_python_sketches/cheeseshop_sketch.txt
    # ./monty_python_sketches/pet_shoppe.txt
    # ./monty_python_sketches/spam_song.txt
#---#
        
#---# Guide Lines 2.0 pt 1:
# Nudge user in direct of correct response if given error when inputting a file name
#---#

print("")
print("----------------------------")
file_question = input("What file would you like to search in? (Choose: cheeseshop_sketch | pet_shoppe | spam_song | NO SPACE AFTER: | ):")
cwd = os.getcwd()
print("----------------------------")
print("")

if file_question == 'cheeseshop_sketch':
    try:
        selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'cheeseshop_sketch.txt')
        with open(selected_file_path, 'r') as file:
            # Do something with the file here, if needed --- this will be word selection / counting etc.
            print("")
            print("----------------------------")
            print("yay file cheeseshop_sketch selected!! :D ")
            print(selected_file_path)
            print("----------------------------")
            print("")
    except FileNotFoundError:
        print("")
        print("----------------------------")
        print('Failed to find the file')
        print("----------------------------")
        print("")
elif file_question == 'pet_shoppe':
    try:
        selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'pet_shoppe.txt')
        with open(selected_file_path, 'r') as file:
            print("")
            print("----------------------------")
            print("yay file pet_shoppe selected!! :D ")
            print(selected_file_path)
            print("----------------------------")
            print("")
    except FileNotFoundError:
        print("")
        print("----------------------------")
        print('Failed to find the file')
        print("----------------------------")
        print("")
elif file_question == 'spam_song':
    try:
        selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'spam_song.txt')
        with open(selected_file_path, 'r') as file:
            print("")
            print("----------------------------")
            print("yay file spam_song selected!! :D ")
            print(selected_file_path)
            print("----------------------------")
            print("")
    except FileNotFoundError:
        print("")
        print("----------------------------")
        print('Failed to find the file')
        print("----------------------------")
        print("")
else:
    print("Could not find file")
    print("Remember:")
    print("NO SPACES [either before or after the file]")
    print("NO CAPITALIZATIONS")
    print("Check for misspelling")
    print("Try again")
    print("")
    print("----------------------------")
    file_question = input("What file would you like to search in? (Choose: cheeseshop_sketch | pet_shoppe | spam_song | NO SPACE AFTER: | ):")
    cwd = os.getcwd()
    print("----------------------------")
    print("")
    if file_question == 'cheeseshop_sketch':
        try:
            selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'cheeseshop_sketch.txt')
            with open(selected_file_path, 'r') as file:
                # Do something with the file here, if needed --- this will be word selection / counting etc.
                print("")
                print("----------------------------")
                print("yay file cheeseshop_sketch selected!! :D ")
                print(selected_file_path)
                print("----------------------------")
                print("")
        except FileNotFoundError:
            print("")
            print("----------------------------")
            print('Failed to find the file')
            print("----------------------------")
            print("")
    elif file_question == 'pet_shoppe':
        try:
            selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'pet_shoppe.txt')
            with open(selected_file_path, 'r') as file:
                print("")
                print("----------------------------")
                print("yay file pet_shoppe selected!! :D ")
                print(selected_file_path)
                print("----------------------------")
                print("")
        except FileNotFoundError:
            print("")
            print("----------------------------")
            print('Failed to find the file')
            print("----------------------------")
            print("")
    elif file_question == 'spam_song':
        try:
            selected_file_path = os.path.join(cwd, 'monty_python_sketches', 'spam_song.txt')
            with open(selected_file_path, 'r') as file:
                print("")
                print("----------------------------")
                print("yay file spam_song selected!! :D ")
                print(selected_file_path)
                print("----------------------------")
                print("")
        except FileNotFoundError:
            print("")
            print("----------------------------")
            print('Failed to find the file')
            print("----------------------------")
            print("")
    else:
        print("Failed to find file")
        exit()
    
#---# Guide Lines pt 3:
# Run program in command line
# ! Ask what word to count in the file that was previously selected
# ! Count the word
# ! Then print the following
        # ! "The word <WORD> was found <NUMBER> time in this file: <FILENAME>."
#---#


#---# Guide Lines 2.0 pt 2:
# Nudge user in direct of correct response if given error when inputting a file name
#---#


print("")
print("----------------------------")
word = input("What word do you want to know the frequency of in this file?: ")
if len(word.split()) > 1:
    print("Enter only a single word")
    word = input("What word do you want to know the frequency of in this file?:")
    if len(word.split()) > 1:
        print("Failed to give one word")
        exit()

#---# Guide Lines 2.0 pt 2:
# case sensitive if the user wants it to be
#---#

case_sensitive = input("Do you want the search to be case sensitive? (y/n): ")
print("----------------------------")
print("")

if case_sensitive.lower() == 'n':
        word = word.lower()

#Searching for the words specified
with open(selected_file_path) as file:
    contents_of_file = file.read()
    total_word = str(contents_of_file).count(word)

#Printing the response
print("")
print("----------------------------")
print(f"The word '{word}' was found '{total_word}' time(s) in this file: {file_question}.")
print("----------------------------")
print("")

print("")
print("----------------------------")
print("Thank you for using Word Counter 1.0!")
print("If you want to check for words in another document rerun the program.")
print("----------------------------")
print("")


