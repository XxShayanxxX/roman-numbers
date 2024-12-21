class IntegerToRoman:
    def __init__(self):
        pass  
    
    def int_to_roman(self, num):
        roman_numeral = ""
        
        # Thousands
        if num >= 1000:
            count = num // 1000
            roman_numeral += "M" * count
            num -= 1000 * count

        # Nine hundreds
        if num >= 900:
            roman_numeral += "CM"
            num -= 900

        # Five hundreds
        if num >= 500:
            roman_numeral += "D"
            num -= 500

        # Four hundreds
        if num >= 400:
            roman_numeral += "CD"
            num -= 400

        # Hundreds
        if num >= 100:
            count = num // 100
            roman_numeral += "C" * count
            num -= 100 * count

        # Ninety
        if num >= 90:
            roman_numeral += "XC"
            num -= 90

        # Fifty
        if num >= 50:
            roman_numeral += "L"
            num -= 50

        # Forty
        if num >= 40:
            roman_numeral += "XL"
            num -= 40

        # Tens
        if num >= 10:
            count = num // 10
            roman_numeral += "X" * count
            num -= 10 * count

        # Nine
        if num >= 9:
            roman_numeral += "IX"
            num -= 9

        # Five
        if num >= 5:
            roman_numeral += "V"
            num -= 5

        # Four
        if num >= 4:
            roman_numeral += "IV"
            num -= 4

        # Ones
        if num >= 1:
            roman_numeral += "I" * num
            num -= num
        
        return roman_numeral


converter = IntegerToRoman()
number = 1987
print(f"The Roman numeral for {number} is {converter.int_to_roman(number)}")
