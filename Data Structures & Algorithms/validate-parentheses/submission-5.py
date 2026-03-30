class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False

        valid_parentheses = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            if char in valid_parentheses:
                if stack and stack[-1] == valid_parentheses[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)

        return not stack