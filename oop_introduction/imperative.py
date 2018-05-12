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
    for item in word_for_number.items():
        key = item[0]
        if n % key == 0:
            found_word = True
            word = item[1]
            print(word, end='')
    if found_word:
        print()
    else:
        print(n)
