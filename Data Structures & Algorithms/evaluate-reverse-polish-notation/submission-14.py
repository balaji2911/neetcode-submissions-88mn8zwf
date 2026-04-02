class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).
        
        Reverse Polish Notation (also known as postfix notation) is a mathematical 
        notation in which every operator follows all of its operands. It eliminates 
        the need for parentheses that are required by infix notation.

        Evaluation Logic:
        - Iterate through the tokens from left to right.
        - If the token is a number, push it onto the stack.
        - If the token is an operator (+, -, *, /), pop the two most recent numbers 
          from the stack. 
        - Apply the operator to those numbers (the first popped is the divisor/subtrahend).
        - Push the resulting value back onto the stack.
        - The final value remaining on the stack is the result.

        Special Handling:
        - Division: Per requirements, division between two integers should truncate 
          toward zero. Python's built-in `int(a / b)` achieves this, whereas `a // b` 
          would floor toward negative infinity.

        Args:
            tokens (List[str]): A list of strings representing a valid RPN expression. 
                                Each string is either a valid integer or an operator 
                                in the set {"+", "-", "*", "/"}.

        Returns:
            int: The integer result of the evaluated expression.

        Raises:
            IndexError: If the input 'tokens' is not a valid RPN expression (e.g., 
                        too many operators for the number of operands).

        Examples:
            >>> sol = Solution()
            >>> sol.evalRPN(["2", "1", "+", "3", "*"])
            9  # ((2 + 1) * 3)
            >>> sol.evalRPN(["4", "13", "5", "/", "+"])
            6  # (4 + (13 / 5))
        """
        stack = []

        for item in tokens:
            # Check if the token is an operator
            if item in "+-*/":
                # LIFO: The second operand is always popped first
                num2 = stack.pop()
                num1 = stack.pop()
                
                if item == '+':
                    stack.append(num1 + num2)
                elif item == '-':
                    stack.append(num1 - num2)
                elif item == '*':
                    stack.append(num1 * num2)
                elif item == '/':
                    # Use float division + int conversion for truncation toward zero
                    stack.append(int(num1 / num2))
            else:
                # Convert string token to integer and push to stack
                stack.append(int(item))
                
        # At the end of a valid RPN expression, exactly one value remains
        return stack[0]