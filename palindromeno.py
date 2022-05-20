class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
    
