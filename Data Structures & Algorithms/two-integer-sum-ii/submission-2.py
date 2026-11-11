class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(numbers):
            x = target - n
            if x in seen:
                return [seen[x], i+1]
            seen[n] = i+1