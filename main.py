def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_words = get_char_counts(text)
    report(book_path, num_words, count_words)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_counts(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in counts:
            counts[lower_char] = 0
        counts[lower_char] += 1
    
    return counts

def report(book_path, num_words, count_words):
    sorted_count_words = sorted_dictionary(count_words)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for dic in sorted_count_words:
        print(f"The '{dic['character']}' character was found {dic['count']} times")
    print("--- End report ---")

def sorted_dictionary(count_words):
    list_count_words = []
    for ch, value in count_words.items():
        if ch.isalpha():
            list_count_words.append({"character": ch, "count": value})

    list_count_words.sort(reverse=True, key=sort_on)
    return list_count_words

def sort_on(dic):
    return dic["count"]

main()
