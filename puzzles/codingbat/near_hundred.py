#
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False


class NearHundred:

    def near_hundred(self, n):
        diff_hundred = abs(100 - n)
        diff_two_hundred = abs(200 - n)

        if diff_hundred <= 10 or diff_two_hundred <= 10:
            return True

        return False
