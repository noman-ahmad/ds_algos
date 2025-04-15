class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''

        if len(word1) < len(word2):
            for i in range(0, len(word1), 1):
                merged_string = merged_string + word1[i] + word2[i]
            
            merged_string = merged_string + word2[-(len(word2)-len(word1)):]

        elif len(word2) < len(word1):
            for i in range(0, len(word2), 1):
                merged_string = merged_string + word1[i] + word2[i]
            
            merged_string = merged_string + word1[-(len(word1)-len(word2)):]
        
        else: 
            for i in range(0, len(word2), 1):
                merged_string = merged_string + word1[i] + word2[i]

        return merged_string