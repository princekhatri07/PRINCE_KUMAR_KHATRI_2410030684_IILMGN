class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
                if (len(nums)== 1):
                    return False
                elif (nums[i] == nums[i-1]):
                    return True
        return False
            
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        