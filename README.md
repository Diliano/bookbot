# BookBot

## Description

BookBot is a simple command-line Python program that reads text from a file, provides insights and generates a report about the text.

## Features

-   Reads text from a specified file
-   Calculates the total word count of the text
-   Analyses the frequency of each letter in the text
-   Generates a comprehensive report with the findings

## Installation

To use BookBot, you will need Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Clone the repository using:

`git clone https://github.com/Diliano/bookbot.git`

## Usage

To run BookBot with the example of "Frankenstein", navigate to the directory containing the script. The `main()` function is set up for this specific example; execute the script using Python:

`python main.py`

### Customising the script for different books

To analyse a different book with BookBot, you need to modify the `main()` function in `main.py`. Here are the steps to do so:

1. **Change the file path:**
-   In the `main()` function, locate the line where `book_path` is set
-   Replace `"books/frankenstein.txt"` with the path to your desired book file. For example:
    ```Python
    book_path = "path/to/your/book.txt"
    ```

2. **Adjust the rest of 'main' function as required:**
-   The rest of the function will process the new text file as it did with "Frankenstein" and can be changed as required to only print the word count for example

3. **Run the script:**
-   After making these changes, save the file and run the script again using `python main.py`