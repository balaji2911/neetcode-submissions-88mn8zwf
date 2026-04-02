class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item.lstrip('-').isdigit():
                stack.append(int(item))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if item == '+':
                    stack.append(num1 + num2)
                elif item == '-':
                    stack.append(num1 - num2)
                elif item == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1/num2))
            print(stack)
                
        return stack[0]

  