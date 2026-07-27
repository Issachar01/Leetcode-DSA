class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "AEIOUaeiou"
        temp = []
        for letter in range(len(s)):
            if s[letter] in vowels:
                temp.append(s[letter])
                s[letter] = '*'
        temp = temp[::-1]
        i = 0
        for letter in range(len(s)):
            if s[letter] == '*':
                s[letter] = temp[i]
                i += 1
        return "".join(s)
