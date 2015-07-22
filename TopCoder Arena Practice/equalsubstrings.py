__author__ = 'justintaing'
# Easy

class EqualSubstrings(object):
    def getSubstrings(self, string):
        """
        :param string: string of lowercase letters
        :return: tuple of strings (x, y), where:
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
    results = sb.getSubstrings("")
    print(results)
