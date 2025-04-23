import sys
from stats import generate_char_list_ascending, count_number_words, generate_char_dictionary_from_text

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def main():
  if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    return

  local_book_path =sys.argv[1]

  book_text = get_book_text(local_book_path)
  word_count = count_number_words(book_text)
  char_list = generate_char_list_ascending(generate_char_dictionary_from_text(book_text))

  print('============ BOOKBOT ============')
  print(f"Analyzing book found at {local_book_path}...")
  print('----------- Word Count ----------')
  print(f"Found {word_count} total words")
  print('--------- Character Count -------')
  for dict in char_list:
    print(f"{dict['char']}: {dict['count']}")
  print('============= END ===============')

main()
