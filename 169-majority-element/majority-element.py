class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        current_majority = 0 

        for num in nums:
            if count == 0: 
                current_majority = num 

            if num == current_majority:
                count += 1
            else:
                count -= 1 

        return current_majority  