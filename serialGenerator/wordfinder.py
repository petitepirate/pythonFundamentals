"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    file = open('complex.txt', 'r')
    ...

    def __init__(self, file='complex.txt'):
        file = list(self.file)  # turn into a list
        res = self.res = [sub[: -2]
                          for sub in file]  # remove last 2 char in each word
        print(f'{len(res)} words read')  # print length of list

    def random(self):
        return random.choice(self.res)  # random selection of edited list


class SpecialWordFinder(WordFinder):

    def trim(self):
        return [w.strip() for w in self.res
                if w.strip() and not w.startswith('#')]
# --------------
# school solution
# import random


# class WordFinder:
#     """Machine for finding random words from dictionary.

#     >>> wf = WordFinder("simple.txt")
#     3 words read

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True
#     """

#     def __init__(self, path):
#         """Read dictionary and reports # items read."""

#         dict_file = open(path)

#         self.words = self.parse(dict_file)

#         print(f"{len(self.words)} words read")

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words."""

#         return [w.strip() for w in dict_file]

#     def random(self):
#         """Return random word."""

#         return random.choice(self.words)


# class SpecialWordFinder(WordFinder):
#     """Specialized WordFinder that excludes blank lines/comments.

#     >>> swf = SpecialWordFinder("complex.txt")
#     3 words read

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True
#     """

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words, skipping blanks/comments."""

#         return [w.strip() for w in dict_file
#                 if w.strip() and not w.startswith("#")]
