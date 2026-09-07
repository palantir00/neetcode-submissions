class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp_dict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in temp_dict:
                return [temp_dict[diff], i]
            temp_dict[n] = i
