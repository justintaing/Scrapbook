__author__ = 'justintaing'
# Easy
# Passes system tests

# PROBLEM STATEMENT
# Julius Caesar used a system of cryptography, now known as Caesar Cipher, which
# shifted each letter 2 places further through the alphabet (e.g. 'A' shifts to
# 'C', 'R' shifts to 'T', etc.). At the end of the alphabet we wrap around, that
# is 'Y' shifts to 'A'.
#
# We can, of course, try shifting by any number. Given an encoded text and a
# number of places to shift, decode it.
#
# For example, "TOPCODER" shifted by 2 places will be encoded as "VQREQFGT". In
# other words, if given (quotes for clarity) "VQREQFGT" and 2 as input, you will
# return "TOPCODER".

class CCipher(object):
    def decode(self, cipherText, shift):
        '''
        :param cipherText: (string) text to decode
        :param shift: (int) amount to shift cipherText
        :return: (string) decoded cipherText
        '''
        import string
        letters = string.ascii_uppercase
        t = string.maketrans(letters, letters[-shift:] + letters[:-shift])

        return cipherText.translate(t)


if __name__ == "__main__":
    cc = CCipher()
    assert cc.decode("VQREQFGT", 2) == "TOPCODER"
    assert cc.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10) == "QRSTUVWXYZABCDEFGHIJKLMNOP"
    assert cc.decode("TOPCODER", 0) == "TOPCODER"
    assert cc.decode("ZWBGLZ", 25) == "AXCHMA"
    assert cc.decode("DBNPCBQ", 1) == "CAMOBAP"
    assert cc.decode("LIPPSASVPH", 4) == "HELLOWORLD"