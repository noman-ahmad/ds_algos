class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ''
        first_itr = 0 
        second_itr = 0

        while True:
            if first_itr >= len(word1) and second_itr >= len(word2):
                break;
            if first_itr < len(word1):
                merged_str += word1[first_itr] 
                first_itr += 1
            if second_itr < len(word2):
                merged_str += word2[second_itr]
                second_itr += 1
            


        
        # if len(word2) > len(word1):
        #     concat_str = word2[-(len(word2) - len(word1)):]
        #     max_itr = len(word1)
        # elif len(word1) > len(word2):
        #     concat_str = word1[-(len(word1) - len(word2)):]
        #     max_itr = len(word2)
        # else:
        #     max_itr = len(word1)

        # for i in range(0, max_itr, 1):
        #     merged_string += word1[i] + word2[i]

        # merged_string += concat_str

        return merged_str