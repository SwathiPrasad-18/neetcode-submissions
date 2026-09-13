class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_s = {}
        s_to_pattern = {}

        for ch, word in zip(pattern, words):

            if ch in pattern_to_s and pattern_to_s[ch] != word:
                return False

            if word in s_to_pattern and s_to_pattern[word] != ch:
                return False

            pattern_to_s[ch] = word
            s_to_pattern[word] = ch

        return True