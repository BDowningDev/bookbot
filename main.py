def main():
      book_path = "books/frankenstein.txt"
      book = get_book_text(book_path)
      word_count = number_of_words(book)
      letter_count = num_each_character(book)
      char_list = [{"char": char, "num": count} for char, count in letter_count.items()]
      char_list.sort(key=sort_by_occurrence, reverse=True)
      print("--- Begin report of books/frankenstein.txt ---")
      print(f"{word_count} words found in the document.")    
      book_report(char_list)

#open book and return text. close when finished
def get_book_text(path):    
        with open(path) as f:
            return f.read()
#split text into list, return length of list
def number_of_words(text):
    words = text.split()   
    return len(words)
#counts how many letters and returns a dictionary {letter: count}
def num_each_character(text):
      my_dic = {}
      for letter in text:
            letter = letter.lower()
            if letter.isalpha():
                  if letter in my_dic:
                        my_dic[letter] += 1
                  else:
                        my_dic[letter] = 1
      return my_dic
#sort variable
def sort_by_occurrence(item):
      return item["num"]
#print function that doesn't need to be its own function
def book_report(list):
      for entry in list:
            print(f"The '{entry["char"]}' character was found {entry["num"]} times")

main()