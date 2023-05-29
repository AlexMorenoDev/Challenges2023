import random
from math import floor
from utils.utils import count_file_lines, get_random_line_from_file

words_source = "<TXT file path>"

class Word:
    def __init__(self):
        num_words = count_file_lines(words_source)
        self.text = get_random_line_from_file(words_source, num_words)

        self.lenght = len(self.text)
        
        max_hidden = random.randint(1, floor(self.lenght * 0.6))
        char_list = list(self.text)

        self.hidden_chars = []
        self.hidden_chars_indexes = []
        for _ in range(max_hidden):
            char_index = random.randint(0, len(char_list)-1)
            self.hidden_chars.append(char_list[char_index])
            self.hidden_chars_indexes.append(char_index)
            char_list[char_index] = '_'
                
        self.incomplete_word = ''.join(char_list)
    
    def show_incomplete(self):
        print("Word status: " + self.incomplete_word)

    def update_incomplete_word(self, typed_char):
        char_list = list(self.incomplete_word)
        while typed_char in self.hidden_chars:
            char_index = self.hidden_chars.index(typed_char)
            hidden_index = self.hidden_chars_indexes[char_index]
            char_list[hidden_index] = typed_char
            self.hidden_chars.remove(typed_char)
            self.hidden_chars_indexes.remove(hidden_index)

        self.incomplete_word = ''.join(char_list)

