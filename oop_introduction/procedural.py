# configurable fizzbuzz

word_for_number = {
    3: 'fizz',
    5: 'buzz',
    7: 'seven',
    8: 'eight'
}

maximum = 100


def run():
    for n in range(1, maximum):
        print_number(n)


def print_number(n):
    found_word = print_words(n)
    if found_word:
        print()
    else:
        print(n)


def print_words(n):
    found_word = False
    for item in word_for_number.items():
        found_word = handle_word(found_word, item, n)
    return found_word


def handle_word(found_word, item, n):
    key = item[0]
    if n % key == 0:
        print_word(item)
        found_word = True
    return found_word


def print_word(item):
    word = item[1]
    print(word, end='')


run()
