# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string, the longest possible,
# containing distinct letters, - each taken only once - coming from s1 or s2.
# Examples:
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
#


class TwoToOne:
    def longest(self, s1, s2):
        result = ""
        index_position = 0
        result_set = list()

        while index_position <= len(s1) - 1:
            if not result_set.count(s1[index_position]):
                result_set.append(s1[index_position])
            index_position += 1

        index_position = 0

        while index_position <= len(s2) - 1:
            if not result_set.count(s2[index_position]):
                result_set.append(s2[index_position])
            index_position += 1

        # sort the list
        result_set.sort()
        for entry in result_set:
            result += entry

        return result
