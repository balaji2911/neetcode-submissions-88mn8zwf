class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False

        valid_parentheses = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            if char in valid_parentheses:
                top_element = stack.pop() if stack else '#'
                if valid_parentheses[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack