class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x%10==0 && x != 0)) {
            return false;
        }
        int Reverted_Number = 0;
        while (x > Reverted_Number) {
            Reverted_Number = Reverted_Number*10 + x%10;
            x/=10;
        }
        return x == Reverted_Number || x == Reverted_Number/10;
    }
};