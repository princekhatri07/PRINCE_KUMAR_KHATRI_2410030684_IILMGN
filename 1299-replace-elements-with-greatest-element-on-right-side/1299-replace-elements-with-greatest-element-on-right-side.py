class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        maxright = -1

        for i in range(n-1,-1,-1):
            curr = arr[i]
            arr[i] = maxright
            maxright = max(maxright,curr)
        return arr


    

       
        