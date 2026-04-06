class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtereds= "".join(ch.lower() for ch in s if ch.isalnum())
        print(filtereds)
        return filtereds == filtereds[::-1]
        