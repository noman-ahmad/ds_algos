class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(); 
        shortest_string = strs[0]

        while len(shortest_string) > 0:
            all_prefixed = True 
            for str in strs:
                if not str.startswith(shortest_string):
                    all_prefixed = False
                    break 
            if all_prefixed: 
                return shortest_string
            else: 
                shortest_string = shortest_string[:-1]
        
        return ""