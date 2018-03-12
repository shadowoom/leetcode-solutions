class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        max = 1
        i = 0
        j = 1
        temp = s[i:j]
        while j < len(s):
            if s[j] not in temp:
                temp = s[i:j+1]
                if len(temp) > max:
                    max = len(temp)
            else:
                i = s.find(s[j], i) + 1
                temp = s[i:j+1]
            j += 1
        return max
        