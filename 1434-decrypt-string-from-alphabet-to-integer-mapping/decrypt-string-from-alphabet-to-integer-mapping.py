class Solution:
    def freqAlphabets(self, s: str) -> str:
        init = []
        s1 = ""
        for i in range(len(s)):
            if s[i] == '#':
                init.pop()
                init.pop()
                init.append(chr(int(s[i-2] + s[i-1]) + 96))
            else:
                init.append(chr(int(s[i]) + 96))

        for i in init:
            s1= s1 + i
        return s1

