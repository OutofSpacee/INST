#Word Counter
  
  #What it can/can't do

    #Allows users to see their current working directory
    #Allows the user to see the files and folders in their current working directory
    #Allows the user to select the directory to search for a word (only works if the ENTIRE path is entered!)
    #Gives the user 3 shots at entering a correct directory
    #If user cannot find directory path they are given the option to quit and exits the program if they type "quit"
    #It does get stuck in an infinate loop if you never quit and you never enter in a correct directory
    #Cannot select a single file, selects entire directory
    #Lets the user type in a word that they would like to search for in the directory that they want
    #The word cannot be longer than ONE word
    #If user enters in more than one word it tells the user to only enter in one word, but there is an endless loop until the user enters in only one word
    #Lets the user choose if the search is to be case sensitive or not
    #Can only look up one word at a time
    #Prints the results to the console and saves them to a file named word_count_results.txt
    #Exits program

  #Instructions

    #Make sure you have Python installed
    #Make sure word_count_04.py is downloaded along with the files that you want to count words in
    #Run the word_count_04.py file
    #Follow the on-screen prompts to input the directory path, word to search for, and case sensitivity preference

Example

    #Suppose you have a directory named monty_python containing several text files. You want to count the occurrences of the word "the" in all files, regardless of case sensitivity.

    Directory Path: /x/y/monty_python
    Word to Search For: the
    Case Sensitivity: no
    The program will search for "python" in all text files within the texts directory, display the results, and save them to a file named word_count_results.txt.
