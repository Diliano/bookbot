def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_text)
    frankeinstein_letters_count_list = get_letters_count_list(frankenstein_text)
    frankenstein_report = get_report(frankenstein_path, frankenstein_word_count, frankeinstein_letters_count_list)
    print(frankenstein_report)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_letters_count_list(book_text):
    letters_dict = {}
    lowered_book_text = book_text.lower()
    for character in lowered_book_text:
        if character.isalpha():
            letter = character
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
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