class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(digits)
        result = []
        for num in range(100, 1000, 2):  # iterate through even 3-digit numbers
            a, b, c = num // 100, (num // 10) % 10, num % 10
            needed = Counter((a, b, c))
            if all(freq[d] >= needed[d] for d in needed):
                result.append(num)
        return result

