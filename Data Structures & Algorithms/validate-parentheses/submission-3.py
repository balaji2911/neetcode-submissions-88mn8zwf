class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            if char not in valid_parentheses.keys():
                stack.append(char)
            else:
                bracket = stack.pop() if stack else False
                if valid_parentheses[char] != bracket:
                    return False

        return len(stack) == 0