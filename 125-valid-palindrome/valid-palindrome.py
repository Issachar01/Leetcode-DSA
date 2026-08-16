class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join([c.lower() for c in s if c.isalnum()])
        if st == st[::-1]:
            return True
        return False
        
