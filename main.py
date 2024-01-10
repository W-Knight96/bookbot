def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letters = count_letters(file_contents)
    report(letters)

def count_words(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

def count_letters(file_contents):
    text = file_contents.lower()
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(d):
    return d["num"] 

def report(letters):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print("Report Start of Frankenstein:\n")
    print(f"The book has {word_count} words\n ")

    sorted_list = []
    for letter in letters:
        sorted_list.append({"letter": letter, "num": letters[letter]})
    sorted_list.sort(reverse = True, key=sort_on)

    for letter in sorted_list:
        if not letter["letter"].isalpha():
            continue
        print(f"The {letter["letter"]} was found {letter["num"]} times")
    
    print("--- Report End ---")

main()
