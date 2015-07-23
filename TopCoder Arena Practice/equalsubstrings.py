__author__ = 'justintaing'
# Easy

# PROBLEM STATEMENT
# You will be given a str consisting of lowercase letters. You will return a
# containing elements x and y in that order. The returned s x and y must
# satisfy:

# 1) The string xy (x with y concatenated on the end) must equal str.
# 2) The number of a's in x must equal the number of b's in y.
# 3) If multiple solutions are possible, use the one that maximizes the length
# of x.

class EqualSubstrings(object):
    def getSubstrings(self, string):
        """
        :param string: (string) lowercase letters
        :return: (tuple: strings) (x, y), where:
            number of a's in x = number of b's in y
        """
        start = 0
        end = len(string)
        mid = (start + end) // 2
        x = string[:mid]
        y = string[mid:]

        while start <= end:
            if x.count('a') == y.count('b'):
                break
            elif x.count('a') < y.count('b'):
                start = mid + 1
            elif x.count('a') > y.count('b'):
                end = mid - 1

            mid = (start + end) // 2
            x = string[:mid]
            y = string[mid:]

        # maximize x
        while len(x) and len(y):
            x += y[0]
            y = y[1:]

            if x.count('a') != y.count('b'):
                y = x[-1] + y
                x = x[:-1]
                break

        return (x, y)


if __name__ == "__main__":
    sb = EqualSubstrings()
    assert sb.getSubstrings("badklsjbasdbfdbfabdfahdbakjhdbasdbf") == ("badklsjbasdbfdbfabdf", "ahdbakjhdbasdbf")
    assert sb.getSubstrings("aaaaaabbbbbbbbb") == ("aaaaaabbb", "bbbbbb")
