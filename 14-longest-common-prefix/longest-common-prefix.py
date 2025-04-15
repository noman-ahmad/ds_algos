class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        shortest_string = None
        for str in strs:
            if shortest_string is None or len(str) < len(shortest_string):
                shortest_string = str

        while len(shortest_string) > 0:
            print(shortest_string)
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