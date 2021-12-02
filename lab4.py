# course: Object-oriented programming, year 2, semester 1
# academic year: 202122
# author: B. Schoen-Phelan
# date: 14-10-2021
# purpose: Lab 4

import sys
import re


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)
        input_list = self.user_input.split()
        char_list = list(self.user_input)
        input_list_length = len(input_list)
        char_list_length = len(char_list)
        char_list_length = char_list_length - 1


        print(input_list)
        new_list = []
        for word in range(0, input_list_length):
            word_length = len(input_list[word])
            # word_length = word_length - 1
            for letter in range(0, char_list_length):
                if char_list_length < 3:
                    pass

                elif " " in char_list[letter]:
                    pass

                elif letter == 0:
                    new_list.append(char_list[letter])

                else:
                    if letter >= 1:
                        letter1 = char_list[letter]
                        letter2 = char_list[letter + 1]

                        char_list[letter] = letter2
                        char_list[letter + 1] = letter1
                        new_list.append(char_list[letter])
            new_list.append(char_list[letter + 1])



        print(input_list)
        print(char_list)
        print(new_list)

        # for letter in range(1, letter_index_length):
        #     if length < 3:
        #         pass
        #
        #     elif new_list[letter] == ' ':
        #         break
        #
        #     else:
        #         letter1 = new_list[letter]
        #         letter2 = new_list[letter + 1]
        #
        #         new_list[letter] = letter2
        #         new_list[letter + 1] = letter1

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

