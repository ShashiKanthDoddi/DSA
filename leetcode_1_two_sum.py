class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (a,i) in enumerate(nums):
            for (b,j) in enumerate(nums):
                if a!=b and i+j==target:
                    return [a,b]
        