def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """

        
    Roman_Version = []

    if num < 1 or num > 3999:
        return "Invalid Value or Beyond Constraints"
    #added this statement due to the original problem in the leetcode constraints
    else:

        Thousands = num // 1000
        if Thousands >= 1:
            Roman_Version.append(Thousands * "M") 

            num = num - Thousands * 1000

        else:

            None

        Hundreds = num // 100
        if Hundreds == 1:
            Roman_Version.append("C")
        elif Hundreds == 2:
            Roman_Version.append("CC")
        elif Hundreds == 3:
            Roman_Version.append("CCC")
        elif Hundreds == 4:
            Roman_Version.append("CD")
        elif Hundreds == 5:
            Roman_Version.append("D")
        elif Hundreds == 6:
            Roman_Version.append("DC")
        elif Hundreds == 7:
            Roman_Version.append("DCC")
        elif Hundreds == 8:
            Roman_Version.append("DCCC")
        elif Hundreds == 9:
            Roman_Version.append("CM")
        else:

            None

        num = num - Hundreds * 100

        Tenths = num // 10

        if Tenths == 1:
            Roman_Version.append("X")
        elif Tenths == 2:
            Roman_Version.append("XX")
        elif Tenths == 3:
            Roman_Version.append("XXX")
        elif Tenths == 4:
            Roman_Version.append("XL")
        elif Tenths == 5:
            Roman_Version.append("L")
        elif Tenths == 6:
            Roman_Version.append("LX")
        elif Tenths == 7:
            Roman_Version.append("LXX")
        elif Tenths == 8:
            Roman_Version.append("LXXX")
        elif Tenths == 9:
            Roman_Version.append("XC")

        else:

            None
               
        num = num - Tenths * 10
        

        if num == 1:
            Roman_Version.append("I")
        elif num == 2:
            Roman_Version.append("II")
        elif num == 3:
            Roman_Version.append("III")
        elif num == 4:
            Roman_Version.append("IV")
        elif num == 5:
            Roman_Version.append("V")
        elif num == 6:
            Roman_Version.append("VI")
        elif num == 7:
            Roman_Version.append("VII")
        elif num == 8:
            Roman_Version.append("VIII")
        elif num == 9:
            Roman_Version.append("IX")

        else:

            None

    Roman_Version_Str = ""
    for item in Roman_Version:

        Roman_Version_Str += item
    return Roman_Version_Str
