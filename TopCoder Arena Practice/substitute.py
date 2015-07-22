__author__ = 'justintaing'
# Easy


class Substitute(object):
    def getValue(self, key, code):
        """
        :param key: string containing key encoding
        :param code: string containing code to decode with key
        :return: int of the decoded code
        """
        result = ""

        for char in code:
            if char in key:
                result += str((key.index(char)+1) % 10)

        return int(result)


if __name__ == "__main__":
    s = Substitute()
    assert s.getValue("TRADINGFEW", "LGXWE") == 709
    assert s.getValue("ABCDEFGHIJ", "XJ") == 0
