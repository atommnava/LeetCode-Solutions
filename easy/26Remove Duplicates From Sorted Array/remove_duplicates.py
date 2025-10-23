class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            # It means we do not have duplicates
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        # Number of elements that are unique
        return j
