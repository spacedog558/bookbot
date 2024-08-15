import os
def main():
    global book_path
    book_path = "books/frankenstein.txt"
    book_content = book_read()
    print(book_content)
    print(f"the number of words is {word_count()}")
    
def book_read():
    with open(book_path) as file:
       return file.read()
def word_count():
    countOfWords = book_read.split()
    return len(countOfWords)


main()

