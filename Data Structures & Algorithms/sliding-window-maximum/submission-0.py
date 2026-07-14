class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements=[]
        l = 0
        maxele,maxidx = nums[0],0

        for i in range(k):
            if nums[i] > maxele:
                maxele = nums[i]
                maxidx=i
        maxElements.append(maxele)

        for r in range(k,len(nums)):
            l+=1
            if l-1 == maxidx:
                maxele,maxidx = -(float('inf')), float('inf')
                for i in range(l,r+1):
                    if nums[i] > maxele:
                        maxele = nums[i]
                        maxidx=i
                maxElements.append(maxele)
                continue
            
            if nums[r] > maxele:
                maxele = nums[r]
                maxidx=r
            maxElements.append(maxele)


        return maxElements

