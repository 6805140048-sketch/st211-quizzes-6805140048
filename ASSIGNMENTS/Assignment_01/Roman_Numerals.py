class roman_numeral:
    values = {     # Defining values for roman numerals
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
#--------------------------------------------------------------------------------------------------------------------------------------
    def convert(self, roman):
        total = 0                                           # start at 0
        prev = 0                                            # keep track of the previous value

        for char in reversed(roman):                        # checks if the input is valid or not
            if char not in self.values:
                raise ValueError("Invalid input value")     # raise a value err if invalid

        for char in reversed(roman):                        # read letters from right to left
            value = self.values[char]                       # find the number for this letter
            if value < prev:                                # if smaller comes before bigger, subtract
                total -= value
            else:                                           # otherwise, add
                total += value
            prev = value                                    # update previous value 

        if self.reverse(total) != roman:                    # check if the structure is correct or not (Example: IIII for 4 instead of IV)
            raise ValueError("Invalid structure!")

        return total
#--------------------------------------------------------------------------------------------------------------------------------------
    def reverse(self, num):                                 # function that convert int to roman numeral
        values = [                                          # defining reversed values
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""                                         # empty str variable because we'll add later with loops

        for value, symbol in values:                        # checks num value and symbol in values variable
            while num >= value:                             # when num from function parameter is >= value, add that symbol and subtract the value
                result += symbol                            # repeats until num = 0
                num -= value

        return result

    