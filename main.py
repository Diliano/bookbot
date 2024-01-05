def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    print(frankenstein_text)
    frankenstein_word_count = get_word_count(frankenstein_text)
    print(frankenstein_word_count)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

main()