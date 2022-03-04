class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix = ""
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix

        return prefix

