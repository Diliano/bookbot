def main():
    frankenstein_path = "books/frankenstein.txt"
    text = get_book_text(frankenstein_path)
    print(text)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()