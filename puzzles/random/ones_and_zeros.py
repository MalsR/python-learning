# Description:
#
# Given an array of one's and zero's convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
#
# Examples:
#
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
#


class OnesAndZeros:

    def ones_and_zeros(self, number_array):

        array_size = len(number_array) - 1
        result = 0

        for array_element in number_array:
            if array_element == 1:
                result += 2**array_size
            array_size -= 1

        return result
