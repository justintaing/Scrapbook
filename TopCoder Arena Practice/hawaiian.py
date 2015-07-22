__author__ = 'justintaing'
# Easy


class Hawaiian(object):
    def isHawaiian(self, word):
        """
        :param word: string
        :return: true if the word is hawaiian, false otherwise
        """
        alpha = {'a', 'e', 'i', 'o', 'u', 'h', 'k', 'l', 'm', 'n', 'p', 'w'}
        leftover = set(word.lower()) - alpha

        return len(leftover) == 0

    def getWords(self, sentence):
        """
        :param sentence: string of words
        :return: tuple of words which are hawaiian
        """
        words = sentence.split(' ')
        hawaiian_words = [word for word in words if self.isHawaiian(word)]

        return tuple(hawaiian_words)


if __name__ == "__main__":
    h = Hawaiian()
    assert h.getWords("Mauna Kea and Mauna Koa are two mountains") == ("Mauna", "Kea", "Mauna", "Koa")
    assert h.getWords("The quick brown fox jumps over the lazy brown dog.") == ()
