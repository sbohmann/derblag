# OOP

Three styles of implementing FizzBuzz

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
        for (key, word) in word_for_number.items():
            if n % key == 0:
                found_word = True
                print(word, end='')
        if found_word:
            print()
        else:
            print(n)

Problem: this nested loop relatively hard to read, even though it's such a simple example.

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
        for (key, word) in word_for_number.items():
            found_word |= handle_word(key, word, n)
        return found_word
    
    
    def handle_word(key, word, n):
        if n % key == 0:
            print_word(word)
            return True
        return False
    
    
    def print_word(word):
        print(word, end='')
    
    
    run()

In a way, this is almost worse... It's really hard to keep track of state. State is all over the place. This is bad for a lot of reasons and allows for extremely hard to analyze bugs.

## OOP

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

Now, the methods are simple, it's very clear where the state resides (in *self*), and the number of aruments has been vastly reduced.

This is the core of OOP. Configuration and state are represented in a very specific place and it's possible to split up methods without ending up with lots of arguments. OOP is simple. 

The same can be achieved in C with a data structure representing the state, and passing a around a pointer to an instance of it, named *self* or similar. That's also OOP.

## OOP in C

It's not particularly pretty but has all the same advantages as in languages with OOP support. The distinction between public and private methods is usually made by only exposing methods in the header file that are considered part of the API.

    #include <stdio.h>
    #include <stdlib.h>
    #include <memory.h>
    
    const int configuration_size = 4;
    int keys[] = { 3, 5, 7, 8 };
    const char * words[] = { "fizz", "buzz", "seven", "eight" };
    const int maximum = 100;
    
    typedef struct  {
        int value;
        int found_word;
    } FizzBuzz;
    
    FizzBuzz * FizzBuzz_create(int value) {
        FizzBuzz *self = malloc(sizeof(FizzBuzz));
        memset(self, 0, sizeof(FizzBuzz));
        self->value = value;
        return self;
    }
    
    void FizzBuzz_print_word(FizzBuzz *self, const char *word) {
        printf("%s", word);
    }
    
    void FizzBuzz_attempt_to_print_word(FizzBuzz *self, int key, const char *word) {
        if (self->value % key == 0) {
            FizzBuzz_print_word(self, word);
            self->found_word = 1;
        }
    }
    
    void FizzBuzz_print_words(FizzBuzz *self) {
        for (int index = 0; index < configuration_size; ++index) {
            FizzBuzz_attempt_to_print_word(self, keys[index], words[index]);
        }
    }
    
    void FizzBuzz_finish_line(FizzBuzz *self) {
        if (self->found_word) {
            printf("\n");
        } else {
            printf("%d\n", self->value);
        }
    }
    
    void FizzBuzz_run(FizzBuzz *self) {
        FizzBuzz_print_words(self);
        FizzBuzz_finish_line(self);
    }
    
    void check_num_words() {
        int fail = 0;
        int number_of_keys = sizeof(keys) / sizeof(int);
        int number_of_words = sizeof(words) / sizeof(const char *);
        if (number_of_keys != configuration_size) {
            fprintf(stderr, "Wrong number of keys: %d\n", number_of_keys);
            fail = 1;
        }
        if (number_of_words != configuration_size) {
            fprintf(stderr, "Wrong number of keys: %d\n", number_of_words);
            fail = 1;
        }
        if (fail) {
            exit(1);
        }
    }
    
    int main() {
        check_num_words();
        
        for (int value = 1; value < maximum; ++value) {
            FizzBuzz *instance = FizzBuzz_create(value);
            FizzBuzz_run(instance);
            free(instance);
        }
    }