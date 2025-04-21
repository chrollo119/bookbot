
import sys
from stats import get_num_words, count_characters, get_sorted_character_report

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{book_path}'")
        sys.exit(1)

    # Get word count
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    # Get character count
    char_counts = count_characters(book_text)
    sorted_report = get_sorted_character_report(char_counts)

    print("\nCharacter Frequency:")
    for item in sorted_report:
        print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()

