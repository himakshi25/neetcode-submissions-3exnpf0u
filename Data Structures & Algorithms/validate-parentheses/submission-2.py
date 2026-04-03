class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '[':
                stack.append(']')
            elif char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            else:
                if stack:
                    print(stack)
                    if char != stack.pop():
                        return False
                else:
                    return False
        
        if not stack:
            return True
        return False