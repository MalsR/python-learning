class ArrayHighAndLowFinder:
    def find(self, number_string):
        high_number = 0
        low_number = 0

        str_split = str.split(number_string, " ")

        # https://docs.python.org/3/library/functions.html#enumerate
        for index, str_element in enumerate(str_split):
            parsed_int = int(str_element)

            if index == 0:
                high_number = parsed_int
                low_number = parsed_int

            if parsed_int > high_number:
                high_number = parsed_int

            if parsed_int < low_number:
                low_number = parsed_int

        return str(high_number) + " " + str(low_number)
