class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  
        left = 0 
        right = len(nums) - 1
        while left <= right:
            if nums[left] != val and nums[right] == val:
                left += 1
            elif nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                k += 1
            elif nums[right] == val and nums[left] == val: 
                right -= 1
                k += 1
            else:
                left += 1
                
        print(nums, k)

        return len(nums) - k