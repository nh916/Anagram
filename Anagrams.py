import re


class Anagrams:

    def __init__(self):
        pass

    def is_anagram(self, phrase1):
        # words = phrase1.split()

        words = re.split(r'\s+', phrase1)

        if len(words) == 0:
            reason = "No words entered! Try Again."
            print(reason)
            return False

        elif len(words) == 1:
            reason = "Only 1 word entered! Cannot be Anagram."
            print(reason)
            return False

        elif len(words) == 2:
            reason = "2 words entered"
            print(reason)

        else:
            reason = "More than 2 words, cannot be anagrams."
            print(reason)
            return False
        # Must be 2 words

        word1 = words[0]
        word2 = words[1]

        if len(word1) != len(word2):
            reason = "Words not same length"
            print(reason)
            return False

        result1 = self.check_anagram(word1, word2)
        if not result1:
            this_not = "not "
        else:
            this_not = ""

        output_anagram = "Input words " + word1 + " and " + word2 + " are " + this_not + "Anagrams."
        print(output_anagram)
        return result1

    def check_anagram(self, word1, word2):
        word_1_characters = list(word1)
        word_1_characters.sort()
        word_2_characters = list(word2)
        word_2_characters.sort()
        characters_in_word_1 = "Word 1 = "

        for char in word_1_characters:
            characters_in_word_1 = characters_in_word_1 + char
        print(characters_in_word_1)

        characters_in_word_2 = "Word 2 = "

        for char in word_2_characters:
            characters_in_word_2 = characters_in_word_2 + char
        print(characters_in_word_2)

        # return Arrays.equals(word_1_characters, word_2_characters);

        if word_1_characters == word_2_characters:
            return True
        else:
            return False


if __name__ == '__main__':
    phrase = Anagrams()
    word_1 = input("Enter Word 1: ")
    word_2 = input('Enter Word 2: ')
    phrase.is_anagram(word_1 + " " + word_2)
