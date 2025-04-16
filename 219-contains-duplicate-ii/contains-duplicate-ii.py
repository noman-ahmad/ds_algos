class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {} 
        for i in range(0, len(nums), 1):
            if nums[i] in hash_map and abs(i - hash_map[nums[i]]) <= k:
                return True
            else:
                hash_map[nums[i]] = i
        return False