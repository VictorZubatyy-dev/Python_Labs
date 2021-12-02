# solution to lab test 1
# OOP Python
# 2021-22
# author: Bianca Schoen-Phelan


class Words:
    def __init__(self):
        file_1 = self.load_file("herbert1.txt", "r")
        file_2 = self.load_file("herbert2.txt", "r")
        stop_words = self.load_file("stops.txt", "r")

        if file_1 and file_2 and stop_words:
            self.find_words(file_1, file_2, stop_words)
        else:
            raise Exception("One of the files is empty")

    # method that loads a file with a specific flag indicating
    # the mode in which a file can be opened, for example "r" for
    # reading, or "w" for writing.
    # The method returns the content of the file in a string.
    # If there was an issue with loading the file it will return
    # an empty variable.
    def load_file(self, file_name, flag):
        try:
            with open(file_name, flag) as the_file:
                lines = the_file.read()
        except FileNotFoundError as fnfe:
            print("The file", file_name, "couldn't be found:" , fnfe)
            return ""
        except Exception as e:
            print("The file", file_name, "has had an issue:" , e)
            return ""
        else:
            # this is the case of no errors
            return lines

    # this method takes three string arguments as input
    # it compares the first two and first finds the words that are
    # common among them and prints them out. Then it finds the words
    # that only exist in one or the other string and prints these out.
    # Then this exercise is repeated but considering the stop words
    # from the third input parameter.
    # This method does not have any return values.
    def find_words(self, sentence_1, sentence_2, stop_words):
        # in order to go through the input it can help to force all
        # words into lower case and split them up by space characters.
        # This is not strictly necessary for the exercise. You can also
        # just work on the strings. This might make it easier.
        a_split = sentence_1.lower().split()
        b_split = sentence_2.lower().split()

        # The test asked you to use a set data type. Both lists are
        # converted into sets. To find the common words we use the
        # intersection method.
        common_words = set(a_split).intersection(set(b_split))
        print("Common words: ", common_words)

        # This does the same as before, but here we go through the list of
        # common words and check if it is a stop word.
        # This specific solution uses a list comprehension. This is not
        # required for your solution but is put here as an FYI. An alternative
        # that does exactly the same could be:
        # common_w_stops = []
        # for word in common_words:
        #     if word not in stop_words:
        #         common_w_stops.append(word)
        common_w_stops = [word for word in common_words if word not in stop_words]
        print("Common words without stop words: ", common_w_stops)

        # here we check which ones of the words is unique to each file and
        # is not shared.
        uncommon_words = set(a_split).symmetric_difference(set(b_split))
        print("Uncommon words: ", uncommon_words)

        # we do the same exercise but considering stop words too
        uncommon_w_stops = [word for word in uncommon_words if word not in stop_words]
        print("Uncommon words without stop words: ", uncommon_w_stops)

# create an instance
# in this program we dont use the instance to access the functions,
# we use innit and self within the class
start = Words()

# creates an instance of the class Words
# w = Words()

# calls the method load_file of the class Words and
# saves the return to a variable
# lines_1 = w.load_file("herbert1.txt", "r")
# lines_2 = w.load_file("herbert2.txt", "r")
# stop_words = w.load_file("stops.txt", "r")

# checks if there is actually anything in the files
# this will fail if there was an issue with loading
# any of the files





