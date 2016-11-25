class CompareThePattern1:
    def pattern(self, number):
        result = ''

        x = 1
        while x <= number:
            y = 1
            while y <= x:
                result += str(x)
                y += 1
            if x != number:
                result += "\n"
            x += 1

        return result
