__author__ = 'justintaing'
# Easy
# Passes system tests

# PROBLEM STATEMENT
# Alien Fred wants to destroy the Earth, but he forgot the password that
# activates the planet destroyer.
#
# You are given a S. Fred remembers that the correct password can be obtained
# from S by erasing exactly one character.
#
# Return the number of different passwords Fred needs to try.

class AlienAndPassword(object):
    def getNumber(self, S):
        """
        :param S: (string) possible characters of the password
        :return: (int) the number of possible passwords
        """
        passwords = {S[:i]+S[i+1:] for i in range(len(S))}
        return len(passwords)


if __name__ == "__main__":
    ap = AlienAndPassword()
    assert ap.getNumber("AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ") == 26
    assert ap.getNumber('A') == 1
    assert ap.getNumber("ZZZZZZZZZZZZZZZZZ") == 1
    assert ap.getNumber("AABACCCCABAA") == 7