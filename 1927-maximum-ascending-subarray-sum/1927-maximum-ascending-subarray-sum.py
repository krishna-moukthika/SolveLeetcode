class Solution(object):
    def maxAscendingSum(self, nums):
        curr = arr_sum = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                curr = curr + nums[i] 
            else:
                curr = nums[i]
            arr_sum = max(arr_sum, curr)
        return arr_sum