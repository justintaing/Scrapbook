__author__ = 'justintaing'
# Easy

# PROBLEM STATEMENT
# You have just begun working as a grocery bagger at the local TopGrocer food
# store. Your job is to place all of a customer's items into bags, so they can
# be carried from the store. Your manager has instructed you to use as few bags
# as possible, to minimize the store's overall cost. However, for the customer's
# convenience, you are instructed that only items of the same type can be
# placed in the same bag. For instance, a produce item can be bagged with any
# other produce items, but not with dairy items.
#
# You are given a itemType indicating the type of each item that needs to be
# bagged. You are also given an strength indicating the maximum number of items
# that can be placed in each bag. You are to return an indicating the minimum
# number of bags required to package the customer's items.

class GroceryBagger(object):
    def minimumBags(self, strength, itemType):
        """
        strength: int between [1, 50]
        itemType: tuple of strings between [1,50] elements
        """
        from math import ceil
        num_bags = 0

        for item in set(itemType):
            num_bags += ceil(itemType.count(item) / float(strength))

        return num_bags

if __name__ == "__main__":
    grocery = GroceryBagger()
    assert grocery.minimumBags(5, ("CANNED", "CANNED", "PRODUCE", "DAIRY",
                                  "MEAT", "BREAD", "HOUSEHOLD", "PRODUCE",
                                  "FROZEN", "PRODUCE", "DAIRY")) == 7

    assert grocery.minimumBags(2, ("CANNED", "CANNED",
                                   "PRODUCE", "PRODUCE")) == 2
