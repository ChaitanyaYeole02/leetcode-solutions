class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0
        result = []

        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                result.append(s[i])
                i += 1
            else:
                result.append(" ")
                j += 1
        
        if i <= len(s):
            result.append(s[i:])
        
        return "".join(result)
