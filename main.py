def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    print(frankenstein_text)
    frankenstein_word_count = get_word_count(frankenstein_text)
    print(frankenstein_word_count)
    print(get_characters_dict(frankenstein_text))

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_characters_dict(book_text):
    characters_dict = {}
    lowered_book_text = book_text.lower()
    for character in lowered_book_text:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

main()