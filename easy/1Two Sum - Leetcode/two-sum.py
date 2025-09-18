class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in num_map:
                return [num_map[complemento], i]

            num_map[num] = i
        return []