class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0
        sumSub = 0
        for r in range(len(arr)):
            sumSub += arr[r]
            if r - l == k - 1:
                if sumSub / k >= threshold:
                    count+=1
                sumSub -= arr[l]
                l+=1
        return  count         