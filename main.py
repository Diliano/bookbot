def main():
    book_path = "books/frankenstein.txt"

    # Try to read the book text; handle any file-related errors
    try:
        book_text = get_book_text(book_path)
    except Exception as e:
        # Print error message if file reading fails and exit the program
        print(f"Error reading file: {e}")
        return
    
    book_word_count = get_word_count(book_text)
    book_letters_dict = get_letters_dict(book_text)
    book_letters_count_list = letters_dict_to_sorted_list(book_letters_dict)
    book_report = get_report(book_path, book_word_count, book_letters_count_list)
    print(book_report)

def get_book_text(book_path):
    # Try to open and read the book file
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        raise FileNotFoundError("The file was not found.")
    except PermissionError:
        raise PermissionError("You do not have permission to read this file.")

def get_word_count(book_text):
    # Return 0 if the book text is empty or None
    if not book_text:
        return 0
    
    words = book_text.split()
    word_count = len(words)

    return word_count

def get_letters_dict(book_text):
    letters_dict = {}

    # Return an empty dictionary if the book text is empty or None
    if not book_text:
        return letters_dict

    # Convert the text to lowercase to ensure consistent counting
    lowered_book_text = book_text.lower()

    for character in lowered_book_text:
        # Check if the character is an alphabetic letter
        if character.isalpha():
            letter = character
            # Add or update the count for each letter in the dictionary
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

    return letters_dict

def letters_dict_to_sorted_list(letters_dict):
    # Return an empty list if the letters dictionary is empty
    if not letters_dict:
        return []

    # Convert the dictionary to a list of tuples
    letters_count_list = list(letters_dict.items())
    # Sort the list by count (second element in each tuple) in descending order
    letters_count_list.sort(key = lambda i: i[1], reverse = True)

    return letters_count_list

def get_report(book_path, word_count, letters_count_list):
    report = f"--- Begin report of {book_path} ---\n"
    
    if word_count == 0:
        report += "No words found in the document\n\n"
    else:
        report += f"{word_count} words found in the document\n\n"

    if not letters_count_list:
        report += "No letter count data found\n"
    else:
        for letter_count in letters_count_list:
            report += f"The '{letter_count[0]}' character was found {letter_count[1]} times\n"

    report += f"--- End report ---"

    return report
     
main()