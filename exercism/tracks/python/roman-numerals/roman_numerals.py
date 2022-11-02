roman = ['I', 'IV', \
             'V', 'IX', \
             'X', 'XL', \
             'L', 'XC', \
             'C', 'CD', \
             'D', 'CM',\
             'M']

deciaml = [1, 4, \
           5, 9, \
            10, 40, \
            50, 90, \
            100, 400, \
            500, 900, \
            1000]

roman_decimal = dict(zip(deciaml, roman))

def roman(number):
    if number == 0: return ''
    index = list(filter(lambda x: x <= number, deciaml))[-1]
    return roman_decimal[index] + roman(number - index)
