class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums = []
        current_prefix = 1
        current_suffix = 1
        for index, num in enumerate(nums):
            if index == 0:
                sums.append(current_prefix)
            else:
                current_prefix *= nums[index - 1]
                sums.append(current_prefix)
        
        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                current_suffix *= nums[i+1]
                sums[i] *= current_suffix

        return sums