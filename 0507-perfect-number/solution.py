class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = 1  # 1 is always a proper divisor

        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i

                if i != num // i:  # avoid adding square root twice
                    s += num // i

            i += 1

        return s == num
