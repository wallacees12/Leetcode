class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # add lend of string and delimator #
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1 #Index to start of string
            j = i + length # Get end index of string
            res.append(s[i:j]) #append
            i = j
            
        return res