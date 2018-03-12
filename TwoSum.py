class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i, num in enumerate(nums):
            if num in my_dict:
                return [my_dict[num],i]
            else:
                my_dict[target-num] = i
        return []
            