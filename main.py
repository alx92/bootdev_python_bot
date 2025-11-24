import sys
from stats import get_word_count
from stats import get_char_count
from stats import build_report
from stats import sort_on

def get_book_text(rel_path):
    with open(rel_path) as f:
        return f.read()

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        res = get_book_text(path)
        num_words = get_word_count(res)
        char_count = get_char_count(res)
        report = build_report(char_count)
        header = "------------ BOOKBOT ------------"
        info = f"Analyzing book found at {path}..."
        header2 = "---------- Word Count ----------"
        info2 = f"Found {num_words} total words"
        char_header = "--------- Character Count -------"
        print(header)
        print(info)
        print(header2)
        print(info2)
        print(char_header)
        report.sort(reverse=True, key=sort_on)
        for item in report:
            if item.get("char").isalpha():
                print(f"{item.get('char')}: {item.get('num')}")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()
