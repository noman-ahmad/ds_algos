class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       ### Assign values to duplicates 
       k = 0
       current_val = None 
       for idx, num in enumerate(nums):
        if current_val is None or num != current_val:
            current_val = num 
        else:
            nums[idx] = 101 
            k += 1

       left = 0 
       right = 0 

       while(right < len(nums)):
        if left == right:
            right += 1
        elif nums[left] != 101 and nums[right] == 101:
            left += 1
            right += 1
        elif nums[left] == 101 and nums[right] != 101:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        elif nums[left] == 101 and nums[right] == 101:
            right += 1
        else:
            left += 1
            right += 1
     
       return len(nums) - k
      
        