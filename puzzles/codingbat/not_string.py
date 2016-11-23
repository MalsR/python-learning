# Given a string, return a new string where "not " has been added to the front. However,
# if the string already begins with "not", return the string unchanged.
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


class NotString:

    def not_string(self, str):
        # include some tests for the fun of it, maybe check str where length is less than three
        first_three_chars = str[:3]

        if "not" == first_three_chars:
            return str

        return "not " + str