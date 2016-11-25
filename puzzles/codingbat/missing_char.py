# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).
#
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'


class MissingChar:

    def missing_char(self, string_to_check, index_pos):
        string_length = len(string_to_check)
        result_string = ""
        index = 0

        while index <= string_length - 1:
            if index != index_pos:
                result_string = result_string + string_to_check[index]
            index += 1

        return result_string

    def missing_char_shorter_way(self, string_to_check, index_pos):
        # from beginning inclusive
        string_prefix = string_to_check[:index_pos]
        # from n + 1 to end (n+1, since n exclusive)
        string_suffix = string_to_check[index_pos + 1:]

        return string_prefix + string_suffix
