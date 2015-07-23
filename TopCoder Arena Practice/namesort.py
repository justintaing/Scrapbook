__author__ = 'justintaing'
# Easy
# Does not pass system tests

# PROBLEM STATEMENT
# A certain business maintains a list of all its customers' names. The list is
# arranged in order of importance, with the last customer in the list being the
# most important. We want to create a new list sorted alphabetically according
# to customers' last names, but among customers with the same last name we want
# the more important ones to appear earlier in the new list. Alphabetical order
# (and equality of last names) should not be case sensitive.
#
# Create a class NameSort that contains a method newList that takes a list of
# names as input and returns the new sorted list as a . The last name of a
# customer is defined to be the part of the name following the last space
# character, or the whole name if it has no space characters. The last name of
# "Bob E Jones" is "Jones". The last name of "Madona" is "Madona".
#
# The names in the new sorted list should retain the same capitalization as they
# had in the original list.

class NameSort(object):
    def merge(self, ls, left, right):
        # This is quite a mess
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i][1] == right[j][1]:
                if len(left[i][0].split()) > len(right[j][0].split()):
                    if left[i][0] < right[j][0]:
                        ls[k] = left[i]
                        i += 1
                    else:
                        ls[k] = right[j]
                        j += 1
                else:
                    ls[k] = right[j]
                    j += 1
            elif left[i][1] < right[j][1]:
                ls[k] = left[i]
                i += 1
            else:
                ls[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            ls[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ls[k] = right[j]
            j += 1
            k += 1

    def mergesort(self, ls):
        if len(ls) > 1:
            mid = len(ls) // 2
            left = ls[:mid]
            right = ls[mid:]

            self.mergesort(left)
            self.mergesort(right)
            self.merge(ls, left, right)

    def newList(self, names):
        """
        :param names: (tuple: strings) names to sort
        :return: (tuple: strings) the sorted names, according to given rules
        """
        last_names = list(map(lambda name: (name, name.lower().split()[-1]), names))
        self.mergesort(last_names)

        return tuple(map(lambda name: name[0], last_names))


if __name__ == "__main__":
    ns = NameSort()
    assert ns.newList(("Tom Jones","ADAMS","BOB ADAMS", "Tom Jones", "STEVE jONeS")) == \
           ("BOB ADAMS", "ADAMS", "STEVE jONeS", "Tom Jones", "Tom Jones")

    assert ns.newList(("C A R Hoare","Kenny G", "A DeForest Hoar","Kenny Gee")) == \
           ("Kenny G", "Kenny Gee", "A DeForest Hoar", "C A R Hoare")
