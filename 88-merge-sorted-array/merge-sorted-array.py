class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        zero_ptr = m 
        i = 0
        j = 0
        while j < len(nums2) and i < len(nums1):
            # print(f"i: {i}, j: {j}")
            if(i >= zero_ptr):
                # print(f"i has surpassed zero ptr: i -> {i}, zero_ptr: {zero_ptr}")
                nums1[zero_ptr] = nums2[j]; 
                zero_ptr += 1
                j += 1
                i += 1
                # print("Updated the list: ", nums1, f"Zero Ptr -> {zero_ptr}, i: {i}, j: {j}")
            elif nums2[j] <= nums1[i]:
                # print("Found Element Less Than Or Equal", f"j -> {j}, nums2[j] -> {nums2[j]}", f"i -> {i}, nums1[i] -> {nums1[i]}")
                move_ptr = zero_ptr
                # print(f"Move Ptr -> {move_ptr}, Zero Ptr -> {zero_ptr}")
                while move_ptr > i:
                    # print("Swapping Elements, Pre: ", nums1, f"Move Ptr -> {move_ptr}")
                    nums1[move_ptr], nums1[move_ptr - 1] = nums1[move_ptr - 1], nums1[move_ptr]
                    # print("Swapping Elements, Post: ", nums1)
                    move_ptr -= 1
                nums1[i] = nums2[j]
                zero_ptr += 1
                j += 1
                # print("Updated the list: ", nums1, f"Zero Ptr -> {zero_ptr}, i: {i}, j: {j}")
            else:
                # print("Element Not Less Or Equal, Updating i")
                i += 1
        

        