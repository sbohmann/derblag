# configurable fizzbuzz

word_for_number = {
    3: 'fizz',
    5: 'buzz',
    7: 'seven',
    8: 'eight'
}

maximum = 100


class NumberPrinter:
    def __init__(self, n):
        self.n = n
        self.found_word = False

    def run(self):
        self._print_words()
        self._finish_line()

    def _finish_line(self):
        if self.found_word:
            print()
        else:
            print(self.n)

    def _print_words(self):
        for (key, word) in word_for_number.items():
            self._handle_word(key, word)

    def _handle_word(self, key, word):
        if self.n % key == 0:
            self._print_word(word)
            self.found_word = True

    def _print_word(self, word):
        print(word, end='')


def run():
    for n in range(1, maximum):
        NumberPrinter(n).run()


run()
