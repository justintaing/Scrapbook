__author__ = 'justintaing'
# Easy

# PROBLEM STATEMENT
# Many languages, including English, French, Spanish, and German use Latin
# characters (a-z). Hawaiian, as well, uses these characters. However, only a
# small subset of these characters are used in the Hawaiian alphabet - the five
# vowels: 'a', 'e', 'i', 'o', 'u', and seven consonants: 'h', 'k', 'l', 'm',
# 'n', 'p', 'w'. Given a sentence of words, you are to determine which could
# possibly be Hawaiian words. Anything which contains a letter not in the
# Hawaiian alphabet cannot be Hawaiian; every other word can be.
#
# A word is defined as a contiguous sequence of letters. You will be given a
# sentence of words. You must tokenize them using a space (' ') as a delimiter,
# remove the words which cannot be Hawaiian, and return the rest in a , in the
# order in which they occur in the sentence, in the same case in which they
# appear in the sentence.

class Hawaiian(object):
    def isHawaiian(self, word):
        '''
        :param word: (string) word to check
        :return: (bool) true if the word is hawaiian, false otherwise
        '''
        alpha = {'a', 'e', 'i', 'o', 'u', 'h', 'k', 'l', 'm', 'n', 'p', 'w'}
        leftover = set(word.lower()) - alpha

        return len(leftover) == 0

    def getWords(self, sentence):
        '''
        :param sentence: (string) words separated with spaces
        :return: (tuple: string) words which are hawaiian
        '''
        words = sentence.split(' ')
        hawaiian_words = [word for word in words if self.isHawaiian(word)]

        return tuple(hawaiian_words)


if __name__ == "__main__":
    h = Hawaiian()
    assert h.getWords("Mauna Kea and Mauna Koa are two mountains") == ("Mauna", "Kea", "Mauna", "Koa")
    assert h.getWords("The quick brown fox jumps over the lazy brown dog.") == ()
