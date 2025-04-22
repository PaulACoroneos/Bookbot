def count_number_words(book_text):
  words = book_text.split()
  return len(words)

def generate_char_dictionary_from_text(book_text):
  dictionary = {}
  lowered_book_text = book_text.lower()
  for char in lowered_book_text:
    if char in dictionary:
      dictionary[char] += 1
    else:
      dictionary[char] = 1
  return dictionary

def generate_char_list_ascending(char_dictionary):
  char_count_list = []
  for char,count in char_dictionary.items():
    if char.isalpha():
      char_count_list.append({'char': char, 'count': count })
  return sorted(char_count_list, key=lambda x: x["count"],reverse=True)