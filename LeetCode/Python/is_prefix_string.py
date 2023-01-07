class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            if prefix == s or len(prefix) > len(s):
                break
            prefix += word
        return prefix == s
