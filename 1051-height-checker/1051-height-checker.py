class Solution(object):
    def heightChecker(self, heights):
        real = sorted(heights)
        count = 0 
        for i in range(0,len(heights)):
            if real[i] != heights[i]:
                count += 1
        return count
                
       