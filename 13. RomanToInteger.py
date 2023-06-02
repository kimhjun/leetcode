class Solution:
    def romanToInt(self, s: str) -> int:
        MAP = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_value = 0
        cur_1, cur_2 = 0, 1
        while cur_1 < cur_2 and cur_1 < len(s):
            if cur_1 == len(s) - 1:
                cur_2 = cur_1
            former, latter = MAP[s[cur_1]], MAP[s[cur_2]]
            if former < latter:
                total_value += (latter - former)
                cur_1 += 2
                cur_2 += 2
            else:
                total_value += former
                cur_1 += 1
                cur_2 += 1
            
        return total_value