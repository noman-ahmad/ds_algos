class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''
        concat_str = '' 
        max_itr = 0
        
        if len(word2) > len(word1):
            concat_str = word2[-(len(word2) - len(word1)):]
            max_itr = len(word1)
        elif len(word1) > len(word2):
            concat_str = word1[-(len(word1) - len(word2)):]
            max_itr = len(word2)
        else:
            max_itr = len(word1)

        for i in range(0, max_itr, 1):
            merged_string += word1[i] + word2[i]

        merged_string += concat_str

        return merged_string