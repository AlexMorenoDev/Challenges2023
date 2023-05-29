import random

def count_file_lines(filepath):
    count = 0
    with open(filepath, 'r') as text_file:
        for line in text_file:
            if line != "\n":
                count += 1

    return count

def get_random_line_from_file(filepath, num_lines):
    word_num = random.randint(1, num_lines)

    count = 1
    text = None
    with open(filepath, 'r') as text_file:
        for line in text_file:
            if count == word_num:
                text = line.rstrip()
                break
            count += 1

    return text