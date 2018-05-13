# configurable fizzbuzz

word_for_number = {
    3: 'fizz',
    5: 'buzz',
    7: 'seven',
    8: 'eight'
}

maximum = 100


class NumberPrinter:
    def __init__(self, value):
        self.value = value
        self.found_word = False

    def run(self):
        self._print_words()
        self._finish_line()

    def _print_words(self):
        for (key, word) in word_for_number.items():
            self._attempt_to_print_word(key, word)

    def _attempt_to_print_word(self, key, word):
        if self.value % key == 0:
            self._print_word(word)
            self.found_word = True

    def _print_word(self, word):
        print(word, end='')

    def _finish_line(self):
        if self.found_word:
            print()
        else:
            print(self.value)


def run():
    for n in range(1, maximum):
        NumberPrinter(n).run()


run()
