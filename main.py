def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_text)
    frankeinstein_letters_dict = get_letters_dict(frankenstein_text)
    print(frankeinstein_letters_dict)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

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

main()