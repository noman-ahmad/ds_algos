class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ''
        first_itr = 0 
        second_itr = 0

        while first_itr < len(word1) or second_itr < len(word2):
            if first_itr < len(word1):
                merged_str += word1[first_itr] 
                first_itr += 1
            if second_itr < len(word2):
                merged_str += word2[second_itr]
                second_itr += 1

        return merged_str