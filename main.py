def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
        letters = count_letters(file_contents)
        print(letters)

def count_words(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)

def count_letters(file_contents):
    text = file_contents.lower()
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters 

main()
