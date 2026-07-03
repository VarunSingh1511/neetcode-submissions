class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hast={}
        ans=[]
        n = len(nums)
        for idx in range(n):
            if nums[idx] in hast:
                continue
            else:
                hast[nums[idx]] = idx
        for i in range(n):
            rn = target - nums[i]
            if rn in hast and i!=hast[rn]:
                if i < hast[rn]:
                    ans.append(i)
                    ans.append(hast[rn])
                else:
                    ans.append(hast[rn])
                    ans.append(i)
                return ans