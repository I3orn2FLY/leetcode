class Solution:

    def intToRoman(self, num: int) -> str:
        total_romans = [['M'], ['C', 'D', 'M'], ['X', 'L', 'C'], ['I', 'V', 'X']]

        degree2values2roman = []
        for degree in range(4):
            values2roman = []
            romans = total_romans[degree]
            for i in range(1, max(4, 10 * (degree != 0))):
                roman = ""
                if i < 4:
                    roman = "".join([romans[0]] * i)
                elif i == 4:
                    roman = romans[0] + romans[1]
                elif i == 5:
                    roman = romans[1]
                elif i < 9:
                    roman = romans[1] + "".join([romans[0]] * (i - 5))
                else:
                    roman = romans[0] + romans[2]

                values2roman.append(roman)
            degree2values2roman.append(values2roman)

        div = 1000
        res = ""
        for i in range(4):
            value = int(num / div)
            num -= div * value
            div /= 10

            if value > 0:
                res += degree2values2roman[i][value - 1]

        return res
