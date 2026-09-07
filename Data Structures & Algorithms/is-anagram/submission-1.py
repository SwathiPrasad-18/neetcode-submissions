class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] +=1
            else:
                freq[ch] = 1
        freq2 = {}
        for char in t:
            if char in freq2:
                freq2[char] +=1
            else:
                freq2[char] = 1
                
        if(freq == freq2):
            return True

        return False