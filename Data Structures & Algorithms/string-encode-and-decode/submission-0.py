class Solution:

    def encode(self, strs: List[str]) -> str:
        result =""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1  : j+1+length])  # Blank 1 & 2
            i = j+1+length                       # Blank 3
        return res
