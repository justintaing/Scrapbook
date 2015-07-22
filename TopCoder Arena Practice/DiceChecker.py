__author__ = 'justintaing'
# Easy
# Passes system tests

# PROBLEM STATEMENT
# The results of rolling a die a number of times is given.  If one particular
# value comes up more than 1/4 of the time, or comes up less than 1/10 of the
# time, the die is considered to be loaded (Loaded means weighted in such a way
# as to make the die show a particular number more or less often than is
# statistically acceptable).
#
# Given a sample of die rolls, decide whether or not the die is loaded, and if
# so, return the numbers that came up too many or too few times.

class DiceChecker(object):
    def badValues(self, values):
        """
        :param values: list of die rolls as ints
        :return: list of sides of the die which are loaded
        """
        num_rolls = len(values)
        loaded_die = []
        for i in range(1, 7):
            side_i_rolls = values.count(i)
            freq = side_i_rolls / float(num_rolls)
            if freq > (1 / 4.) or freq < (1 / 10.):
                loaded_die.append(i)

        return loaded_die


if __name__ == "__main__":
    dc = DiceChecker()
    assert dc.badValues([1, 1, 3, 3, 4, 4, 2, 2, 5, 5, 6, 6]) == []
    assert dc.badValues([3, 1, 5]) == [1, 2, 3, 4, 5, 6]
