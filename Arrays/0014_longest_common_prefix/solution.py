class Solution(object):

    def longestCommonPrefix(self, strs):

        for i in range(min([len(word) for word in strs])):
            for word in strs:
                if strs[0][i] != word[i]:
                    return strs[0][:i]

        return strs[0][:min([len(word) for word in strs])]



