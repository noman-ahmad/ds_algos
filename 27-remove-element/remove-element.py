class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        for i in range(0, len(nums), 1):
            if nums[i] == val:
                k += 1 
                nums[i] = -1 

        nums.sort(reverse=True); 

        return len(nums) - k