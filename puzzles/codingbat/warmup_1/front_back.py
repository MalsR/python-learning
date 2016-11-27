# Given a string, return a new string where the first and last chars have been exchanged.
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'


class FrontBack:

    def front_back(self, string_to_swap):
        if len(string_to_swap) == 1:
            return string_to_swap
        else:
            front_char = string_to_swap[0]
            rear_char = string_to_swap[len(string_to_swap) - 1]
            middle_string = string_to_swap[1:len(string_to_swap) - 1]
            return rear_char + middle_string + front_char
