import os

def list_files_in_directory(directory_path):
    """
    Lists files in directory
    """
    try:
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{directory_path}' not found.")


def count_word_in_file(word, file_path, case_sensitive=True):
    """
    Counts word in file
    
    Args:
        The word to count
        The path to the file
        Whether to consider case sensitivity (default is True)
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not case_sensitive:
                content = content.lower()
            count = content.count(word.lower() if not case_sensitive else word)
            return count
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")

def search_word_in_directory(word, directory_path, case_sensitive=True):
    """
    Searches for a word in all files within a directory.
    
    Args:
    Same as count_word_in_file
    """
    results = []
    files = list_files_in_directory(directory_path)
    if files is None:
        raise FileNotFoundError(f"No files found in directory '{directory_path}'.")
    
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        #uses the previous def to count the word in the files
        count = count_word_in_file(word, file_path, case_sensitive)
        if count != -1:
            results.append((file_path, count))
    return results

def print_and_save_results(results, word):
    """
    Prints and saves the word count results to a file.
    """
    with open("word_count_results.txt", 'w') as output_file:
        for file_path, count in results:
            output = f"The word '{word}' was found {count} times in the file! File: {file_path}"
            print(output)
            output_file.write(output + '\n')



attempts = 0
    
    # Display welcome message
print("----------------------------")
print("Welcome to Word Counter Final!")
print("----------------------------")
    
# Display current working directory
cwd = os.getcwd()
print("\n----------------------------")
print("Current working directory:", cwd)
print("----------------------------\n")
    
# List files and folders in the directory
print("----------------------------")
print("Files and folders in the directory:")
print(os.listdir())
print("----------------------------\n")
    
# Connect to the chosen directory
while True:
    directory_path = input("Enter the path to the directory [Make sure it is the ENTIRE path that you want to go to!]: ")
    if not os.path.isdir(directory_path):
        attempts += 1
        #allowing the user to input multiple times but once it reaches 3rd time it then asks if them want to quit
        if attempts >= 3:
            quit_option = input("Failed to find directory. Enter 'quit' to exit the program: ")
            if quit_option.lower() == 'quit':
                print("Exiting the program.")
                exit()
            else:
                #Restarts the number of attemps, therefore this loops if the user does not type quit
                attempts = 0
        elif attempts == 2:
            print("You have one more attempt remaining.")
        else:
            print("Invalid directory path. Please try again.")
    else:
        break
    
# Enter the word and choose if it is case sensitive
word = input("Enter the word to search for: ")
    #Making sure there is only one word
while ' ' in word:
    print("Error: Please enter only a single word.")
    word = input("Enter the word to search for: ")
    
case_sensitive_input = input("Do you want the search to be case sensitive? (yes/no): ")
if case_sensitive_input.lower() not in ['yes', 'no']:
        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
case_sensitive = case_sensitive_input.lower() == "yes"
    
    # Search for the words in the file
results = search_word_in_directory(word, directory_path, case_sensitive)
if results is None:
        print("Failed to list files in the directory.")
    
    # Print and save the results

print("\n----------------------------")
print_and_save_results(results, word)
print("----------------------------\n")
    
print("\n----------------------------")
print("Results have been saved to 'word_count_results.txt'.")
print("----------------------------\n")



# Test Case 1: Make sure to run full code above then put in the following answers to the following questions:

    # Q1 Enter the path to the directory [Make sure it is the ENTIRE path that you want to go to!]: 
        # A1 C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches
    # Q2 Enter the word to search for:
        # A2 the
    # Q3 Do you want the search to be case sensitive? (yes/no): 
        # A3 no
#Results:
    #The word 'the' was found 26 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\cheeseshop_sketch.txt
    #The word 'the' was found 54 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\pet_shoppe.txt
    #The word 'the' was found 10 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\spam_song.txt

#Test Case 2: Make sure to run full code above then put in the following answers to the following questions:

    # Q1 Enter the path to the directory [Make sure it is the ENTIRE path that you want to go to!]:
        # A1 C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches
    # Q2 Enter the word to search for:
        # A2 Cheese
    # Q3 Do you want the search to be case sensitive? (yes/no): 
        # A3 yes
#Results:
    #The word 'Cheese' was found 4 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\cheeseshop_sketch.txt
    #The word 'Cheese' was found 0 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\pet_shoppe.txt
    #The word 'Cheese' was found 0 times in the file! File: C:\Users\rosea\INST 126\word_count_program\word_count_program\monty_python_sketches\spam_song.txt
