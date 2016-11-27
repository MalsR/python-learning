# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.
#
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'


class FrontThree:

    def front_three(self, str):
        if len(str) <= 3:
            return str + str + str

        string_prefix = str[:3]
        return string_prefix + string_prefix + string_prefix
