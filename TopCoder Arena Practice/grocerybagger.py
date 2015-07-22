__author__ = 'justintaing'
# Easy


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
