import sys # Import the sys module for command-line arguments

# Define functions to process the book text and generate statistics
# These functions would typically be in a 'stats.py' file

def get_book_text(path: str) -> str:
    """Reads the content of the book from the given path."""
    with open(path) as f:
        return f.read()

def get_num_words(text: str) -> int:
    """Counts the number of words in the text."""
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict:
    """Counts the occurrences of each character in the text (case-insensitive)."""
    char_dict = {}
    for char in text.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def get_sorted_char_report_list(char_counts_dict: dict) -> list:
    """
    Converts a dictionary of character counts to a list of dictionaries,
    with each dictionary containing 'char' and 'num' keys.
    The list is sorted by 'num' in descending order.
    """
    report_list = []
    for char, count in char_counts_dict.items():
        report_list.append({"char": char, "num": count})
    
    # Sort the list of dictionaries by the "num" value in descending order
    report_list.sort(key=lambda item: item["num"], reverse=True)
    return report_list

# Define the main function to orchestrate the analysis and reporting
# This function would typically be in a 'main.py' file

def main():
    """
    Main function to analyze the book and print the report.
    Accepts book path as a command-line argument.
    """
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with status code 1 indicating an error
    
    book_path = sys.argv[1] # Get the book path from the command-line argument

    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("-" * 30) # Separator line for clarity

    try:
        # Get the text from the book
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The book at '{book_path}' was not found.")
        print("Ensure the file exists and the path is correct.")
        print("============= END ===============")
        sys.exit(1) # Exit if file not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        print("============= END ===============")
        sys.exit(1) # Exit on other file reading errors


    # Get the number of words
    num_words = get_num_words(text)
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-" * 30) # Separator line

    # Get character counts
    char_counts = get_char_count(text)
    
    # Get the sorted list for the character report
    sorted_char_list = get_sorted_char_report_list(char_counts)
    
    # Print character count section
    print("--------- Character Count -------")
    for item in sorted_char_list:
        char = item["char"]
        num = item["num"]
        # Print only alphabetic characters as per the requirement
        if char.isalpha():
            print(f"{char}: {num}")
            
    # Print report footer
    print("============= END ===============")

if __name__ == "__main__":
    main()