class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s_list = list(s)
        left_ptr = 0
        right_ptr = len(s_list) - 1
        while left_ptr <= right_ptr:
            left_char = s_list[left_ptr].lower()
            right_char = s_list[right_ptr].lower()
            if all(c in vowels for c in [left_char, right_char]):
                s_list[left_ptr], s_list[right_ptr] = (
                    s_list[right_ptr],
                    s_list[left_ptr],
                )
                left_ptr += 1
                right_ptr -= 1 
            elif left_char in vowels:
                right_ptr -= 1
            elif right_char in vowels: 
                left_ptr += 1
            else: 
                left_ptr += 1
                right_ptr -= 1
        return ''.join(s_list)
