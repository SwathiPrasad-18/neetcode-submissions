class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]


        for ch in strs:
            while not ch.startswith(prefix):
                prefix = prefix[:-1]
            
            if prefix == "":
                return ""
        return prefix