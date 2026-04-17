class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): #each char in first string
            for string in strs[1:]: # from second string
                if len(string)<=i or string[i]!=strs[0][i]: #if current string size is shorter than index or element mismatch
                    return strs[0][:i] # return the prefix of reference string not including i
        return strs[0]