class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for c in s:
                res = res + str(ord(c)) + "/"
            res = res + "#"
        return res

    def decode(self, s: str) -> List[str]:
        ls=[]
        word=""
        num = ""
        for c in s:
            if c == "#":
                ls.append(word)
                word = ""
            elif c=="/":
                word = word + chr(int(num))
                num = ""
            else:
                num = num + c
        return ls


