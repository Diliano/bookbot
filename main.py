def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_text)
    frankeinstein_letters_count_list = get_letters_count_list(frankenstein_text)
    print(frankeinstein_letters_count_list)

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
     
main()