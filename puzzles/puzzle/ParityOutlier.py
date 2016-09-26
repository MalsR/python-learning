class ParityOutlier:
    def find(self, number):
        odd_numbers = []
        even_numbers = []

        for number_to_check in number:
            if number_to_check % 2 != 0:
                odd_numbers.append(number_to_check)
            else:
                even_numbers.append(number_to_check)

        if len(odd_numbers) > len(even_numbers):
            return even_numbers[0]
        else:
            return odd_numbers[0]
