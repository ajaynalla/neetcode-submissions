class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, x in enumerate(nums):
            seen = target - x
            if seen in res:
                return [res[seen], i]
            res[x] = i
        
        return res