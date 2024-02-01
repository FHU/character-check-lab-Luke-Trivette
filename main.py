#Remove pass and complete the code
def check_character(word, index):
    if 0 < index < len(word):
        char_at_index = word[index]
    if char_at_index.isalpha():
        return "letter"
    elif char_at_index.isdigit():
      return "number"
    elif char_at_index.isspace():
      return "whitespace"
    else:
      return "unknown"
    
    
   
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))