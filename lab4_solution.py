# course: Object-oriented programming, year 2, semester 1
# academic year: 202122
# author: B. Schoen-Phelan
# date: 14-10-2021
# purpose: Lab 4


import sys

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        # if len(self.user_input) > 3:
        #     new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] \
        #                + self.user_input[3:]
        # elif len(self.user_input) <= 3:
        #     new_word = self.user_input
        # else: # here we assume this word is just one character long or the space character
        #     print("try again")
        #     new_word = False
        #
        # print(new_word)

        # one solution for full sentence
        sentence = self.user_input.strip().split()

        # Get the word from the sentence
        for index, word in enumerate(sentence):
            # check the length of the word > 3
            if len(word) > 3:
                # swap the indice of 2 and last element
                temp_word = list(word) # we use a list for item assignment, but could also just use another new string variable
                if (',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    # split the word in to a list of characters and swap
                    # this swap leaves first and last in tact
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                # Join the characters together and form the word
                swapped_word = ''.join(temp_word)
                # replace the previous word at that position with the new swapped word
                sentence[index] = swapped_word
            else:
                # Since the length of the word < 3 don't swap the word
                sentence[index] = word

        # Join all the words with a space
        the_swap = ' '.join(sentence)
        # Print word
        print(the_swap)

word_scrambler = WordScramble()
word_scrambler.scramble()
# print(string.punctuation)
