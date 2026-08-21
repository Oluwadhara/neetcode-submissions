class Solution:
    def isPalindrome(self, s: str) -> bool:
        ogstr = ""
        for c in s:
            if c.isalnum():
                ogstr += c.lower()
        return ogstr == ogstr[::-1]