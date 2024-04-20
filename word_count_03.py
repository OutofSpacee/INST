import os

def list_files_in_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        return None

def count_word_in_file(word, file_path, case_sensitive=True):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not case_sensitive:
                content = content.lower()
            count = content.count(word.lower() if not case_sensitive else word)
            return count
    except FileNotFoundError:
        return -1

def search_word_in_directory(word, directory_path, case_sensitive=True):
    results = []
    files = list_files_in_directory(directory_path)
    if files is None:
        return None
    
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        count = count_word_in_file(word, file_path, case_sensitive)
        if count != -1:
            results.append((file_path, count))
    return results

# Making sure to save the results ontop of printing the word count 
def print_and_save_results(results, word):
    with open("word_count_results.txt", 'w') as output_file:
        for file_path, count in results:
            output = f"The word '{word}' was found {count} times in the file! File: {file_path}"
            print(output)
            print("Thank you for using Word Counter 3.0")
            output_file.write(output + '\n')


attempts = 0
cwd = os.getcwd()

print("----------------------------")
print("Welcome to Word Counter 3.0!")
print("----------------------------")

# Display current working directory
print("")
print("----------------------------")
print("Current working directory:", cwd)
print("----------------------------")
print("")
   

# List files and folders in the directory
print("")
print("----------------------------")
print("Files and folders in the directory:")
print(os.listdir())
print("----------------------------")
print("")

# Connecting to the chosen directory that the user inputs
while True:
    directory_path = input("Enter the path to the directory [Make sure it is the ENTIRE path that you want to go to!]: ")
    if not os.path.isdir(directory_path):
        attempts += 1
        if attempts >= 3:
            quit_option = input("Failed to find directory. Enter 'quit' to exit the program: ")
            if quit_option.lower() == 'quit':
                print("Exiting the program.")
            else:
                attempts = 0
        print("Invalid directory path. Please try again.")

    else:
        break
# Entering in the word and choosing if it is case sensitive
word = input("Enter the word to search for: ")
while ' ' in word:
    print("Error: Please enter only a single word.")
    word = input("Enter the word to search for: ")

case_sensitive_input = input("Do you want the search to be case sensitive? (yes/no): ")
case_sensitive = case_sensitive_input.lower() == "yes"

# Searching for the words in the file
results = search_word_in_directory(word, directory_path, case_sensitive)
if results is None:
    print("Failed to list files in the directory.")
    

# Printing the results
    
print("")
print("----------------------------")
print_and_save_results(results, word)
print("----------------------------")
print("")

print("")
print("----------------------------")
print("Results have been saved to 'word_count_results.txt'.")
print("----------------------------")
print("")

