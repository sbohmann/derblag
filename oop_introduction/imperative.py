# configurable fizzbuzz

word_for_number = {
    3: 'fizz',
    5: 'buzz',
    7: 'seven',
    8: 'eight'
}

maximum = 100

for n in range(1, maximum):
    found_word = False
    for (key, word) in word_for_number.items():
        if n % key == 0:
            found_word = True
            print(word, end='')
    if found_word:
        print()
    else:
        print(n)
