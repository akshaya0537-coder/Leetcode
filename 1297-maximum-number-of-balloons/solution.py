class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter=defaultdict(int)
        ball='balloon'
        for i in text:
            if i in ball:
                counter[i]+=1
        if any(i not in counter for i in ball):
            return 0
        else:
            return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
