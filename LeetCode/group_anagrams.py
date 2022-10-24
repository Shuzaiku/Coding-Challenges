class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pointer = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if not sorted_word in pointer:
                pointer[sorted_word] = [word]
            else:
                pointer[sorted_word].append(word)
        return list(pointer.values())
