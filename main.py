import sys
from stats import get_book_text, get_num_words, get_char_counts, report

def main():
    arg_list = sys.argv
    if len(arg_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = arg_list[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_words = get_char_counts(text)
    report(book_path, num_words, count_words)

main()
