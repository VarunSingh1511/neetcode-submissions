class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0
        subArr=[]
        for r in range(len(arr)):
            subArr.append(arr[r])
            if r - l == k - 1:
                if sum(subArr) /len(subArr) >= threshold:
                    count+=1
                subArr.remove(arr[l])
                l+=1
        return  count         