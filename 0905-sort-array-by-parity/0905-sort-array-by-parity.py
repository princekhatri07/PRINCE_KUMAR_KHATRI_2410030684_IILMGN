class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)

        if n == 1:
            return nums

        i = 0
        j = 0

        while j < n:
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        return nums