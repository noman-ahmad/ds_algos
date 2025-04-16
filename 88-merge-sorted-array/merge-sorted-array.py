class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        zero_ptr = m 
        i = 0
        j = 0
        while j < len(nums2) and i < len(nums1):
            if(i >= zero_ptr):
                nums1[zero_ptr] = nums2[j]; 
                zero_ptr += 1
                j += 1
                i += 1
            elif nums2[j] <= nums1[i]:
                move_ptr = zero_ptr
                while move_ptr > i:
                    nums1[move_ptr], nums1[move_ptr - 1] = nums1[move_ptr - 1], nums1[move_ptr]
                    move_ptr -= 1
                nums1[i] = nums2[j]
                zero_ptr += 1
                j += 1
            else:
                i += 1
        

        