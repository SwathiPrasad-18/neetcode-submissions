class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = s.split()[-1]
        lastword = len(r)

        return lastword