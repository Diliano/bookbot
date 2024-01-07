def main():
    frankenstein_path = "books/frankenstein.txt"
    try:
        frankenstein_text = get_book_text(frankenstein_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    frankenstein_word_count = get_word_count(frankenstein_text)
    frankenstein_letters_dict = get_letters_dict(frankenstein_text)
    frankenstein_letters_count_list = letters_dict_to_sorted_list(frankenstein_letters_dict)
    frankenstein_report = get_report(frankenstein_path, frankenstein_word_count, frankenstein_letters_count_list)
    print(frankenstein_report)

def get_book_text(book_path):
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        raise FileNotFoundError("The file was not found.")
    except PermissionError:
        raise PermissionError("You do not have permission to read this file.")

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_letters_dict(book_text):
    letters_dict = {}
    lowered_book_text = book_text.lower()
    for character in lowered_book_text:
        if character.isalpha():
            letter = character
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict

def letters_dict_to_sorted_list(letters_dict):
    letters_count_list = list(letters_dict.items())
    letters_count_list.sort(key = lambda i: i[1], reverse = True)
    return letters_count_list

def get_report(book_path, word_count, letters_count_list):
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{word_count} words found in the document\n\n"
    for letter_count in letters_count_list:
        report += f"The '{letter_count[0]}' character was found {letter_count[1]} times\n"
    report += f"--- End report ---"
    return report
     
main()