class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasht={}
        output=[]
        for i in nums:
            if i in hasht:
                hasht[i]+=1
            else:
                hasht[i]=1
        sortedMap = dict(sorted(hasht.items(), key=lambda item: item[1], reverse=True))
        lkeys = list(sortedMap.keys())
        for j in range(k):
            output.append(lkeys[j])
        return output