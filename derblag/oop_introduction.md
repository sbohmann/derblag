# OOP

The precursors

## Common code for all examples

    word_for_number = {
        3: 'fizz',
        5: 'buzz',
        7: 'seven',
        8: 'eight'
    }
    
    maximum = 100

## Imperative style
    
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

Problem: the nested loop is in no way, shape, or form readable.

## Procedural style

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

In a way, this is almost worse... It's really hard to keep track of state. State is all over the place. This is bad for a lot of reasons and allows for extremely hard to analyze bugs.

## OOP

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
            for item in word_for_number.items():
                self._handle_word(item)
    
        def _handle_word(self, item):
            key = item[0]
            if self.n % key == 0:
                self._print_word(item)
                self.found_word = True
    
        def _print_word(self, item):
            word = item[1]
            print(word, end='')
    
    
    def run():
        for n in range(1, maximum):
            NumberPrinter(n).run()
    
    
    run()

Now, the methods are simple, it's very clear where the state resides (in *self*), and the number of aruments has been vastly reduced.

This is the core of OOP. Configuration and state are represented in a very specific place and it's possible to split up methods without ending up with lots of arguments. OOP is simple. 

The same can be achieved in C with a data structure representing the state, and passing a around a pointer to an instance of it, named *self* or similar. That's also OOP.
