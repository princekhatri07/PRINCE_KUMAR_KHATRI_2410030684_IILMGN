class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        curr = 0
        for i in range(0,len(nums)):

            if nums[i] == 1:
             count += 1

            else :
                if count >curr:
                    curr = count
                
                count = 0
        return max(curr,count)

        

         
                
            
    


                
       
        