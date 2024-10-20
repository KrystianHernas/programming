# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# - 1 <= strs.length <= 200
# - 0 <= strs[i].length <= 200
# - strs[i] consists of only lowercase English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        temp = ""
        if strs == [""]:
            return ""
        for i in range(1, len(strs)):
            if strs[i-1] == "" or strs[i] == "":
                return ""
            if strs[0][0] !=  strs[i][0]:
                return ""
        str = strs[0][0]
        for j in range(1, len(min(strs, key=len))):
            for i in range(0, len(strs)):
                print(strs[i][j])
                for k in range(1, len(strs)):
                    if strs[i][j] == strs[k][j]:
                        temp = strs[i][j]
                    else:
                        return str
            str+=temp
        return str

strs = [["flower","flow","flight"], ["dog","racecar","car"]]
for i in strs:
    Solution.longestCommonPrefix(strs=strs[i])