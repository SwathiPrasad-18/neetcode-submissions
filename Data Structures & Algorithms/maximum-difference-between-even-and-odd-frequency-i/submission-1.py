class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        a1 = float('inf')
        a2 = 0

        for count in freq.values():
            if count % 2 == 0:
                a1 = min(a1, count)
            else:
                a2 = max(a2, count)
            
        return a2 - a1