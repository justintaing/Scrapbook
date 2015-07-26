__author__ = 'justintaing'
# Easy
# Does not pass system tests

# PROBLEM STATEMENT
# A p is called anti-palindrome if p[i] doesn't equal to p[n - i - 1] for each
# 0 <= i < (n-1)/2, where n is the length of p. It means that each character
# (except the middle in the case of a string of odd length) must be different
# from its symmetric character. For example, "c", "cpp", "java" are
# anti-palindrome, but "test", "pp" and "weather" are not.
#
# You are given a s. Rearrange its letters in such a way that the resulting
# string is anti-palindrome. If there are several solutions, return the one that
# comes earliest alphabetically. If it is impossible to do it, return the empty
# string.

class AntiPalindrome(object):
    def is_anti(self, word):
        '''
        :param word: (string) word to check
        :return: (bool) true if the word is an antipalindrome, false otherwise
        '''
        if len(word) <= 1:
            return True
        elif word[0] != word[-1]:
            return True and self.is_anti(word[1:-1])
        else:
            return False

    def rearrange(self, s):
        '''
        :param s: (string) word to rearrange into an antipalindrome
        :return: (string) rearranged word
        '''
        from itertools import permutations
        num_char = len(set(s))

        if num_char == 1:
            return ""

        letters = sorted(list(s))
        mid = len(letters) // 2
        left = letters[:mid]
        right = letters[mid:]

        result = ''.join(left+right)

        # This part is non-optimal;
        # does not consider left half of string and may have poor runtimes
        if not self.is_anti(result):
            for i in permutations(right):
                right = list(i)
                result = ''.join(left+right)
                if self.is_anti(result):
                    break

        return result


if __name__ == "__main__":
    ap = AntiPalindrome()
    assert ap.rearrange("test") == "estt"
    assert ap.rearrange("reflectionnoitcelfer") == "cceeeeffiillnnoorrtt"

