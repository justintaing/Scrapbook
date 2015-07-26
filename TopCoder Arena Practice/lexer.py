__author__ = 'justintaing'
# Easy
# Passes system tests

# PROBLEM STATEMENT
# A lexer (lexical analyzer) is used in compilers to break input text into
# pieces called tokens. In this problem you will be given a list of valid
# tokens. For example:
# tokens = {"ab","aba","A"}
#
# Given a list of valid tokens and an input string your lexer will work as
# follows:
# 1) a) If the input doesn't begin with one of the valid tokens, remove the
# first character from the string.
# b) If the input does begin with a valid token, determine the longest valid
# token the input starts with and remove it from the string. The removed portion
# is considered CONSUMED.
# 2) Repeat 1 until there are no characters left in the input.
#
# The lexer is CASE-SENSITIVE so a token must exactly match the beginning of the
# string.
#
# Given a list of valid tokens and an input string your method will return a
# list containing the CONSUMED valid tokens in the order they were CONSUMED.
# For example:
# tokens = {"ab","aba","A"}
# input = "ababbbaAab"
#
# "ab" and "aba" are found at the beginning of the input but "aba" is longest so
# it is consumed. Now:
# consumed = {"aba"}
# input = "bbbaAab"
#
# There are no tokens that start with 'b' so the lexer will remove the first 3
# characters from the string.
# consumed = {"aba"}
# input = "aAab"
#
# The 'a' doesn't match the token "A" due to CASE-SENSITIVITY. The lexer removes
# the 'a' from the beginning of the string.
# consumed = {"aba"}
# input = "Aab"
#
# The lexer consumes the "A" token.
# consumed = {"aba","A"}
# input = "ab"
#
# Finally the lexer consumes the "ab" token and completes the process.
# consumed = {"aba","A","ab"}
# input = ""
# The returned list is {"aba","A","ab"}.
#
# Create a class Lexer that contains the method tokenize, which takes a tokens,
# and a input, and returns a in the form specified above.

class Lexer(object):
    def tokenize(self, tokens, input):
        '''
        :param tokens: (tuple: strings) tokens
        :param input: (string) input to check for tokens
        :return: (tuple: string) tokens in order of when they were removed from
            the input string
        '''
        removed = ()

        while input:
            tokens_found = [t for t in tokens if input.find(t) == 0]

            if tokens_found:
                longest = max(tokens_found, key=len)

                removed += (input[:len(longest)],)
                input = input[len(longest):]
            else:
                input = input[1:]

        return removed


if __name__ == "__main__":
    l = Lexer()
    assert l.tokenize(("ab","aba","A"), "ababbbaAab") == ("aba", "A", "ab")
    assert l.tokenize(("wow","wo","w"), "awofwwofowwowowowwwooo") == ("wo", "w", "wo", "w", "wow", "wow", "w", "wo")
    assert l.tokenize(("AbCd","dEfG","GhIj"), "abCdEfGhIjAbCdEfGhIj") == ("dEfG", "AbCd", "GhIj")
