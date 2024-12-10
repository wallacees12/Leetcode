from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def push(n: int):
            stack.append(n)

        def pop() -> int:
            return stack.pop()

        for e in tokens:
            if e.lstrip("-").isdigit():  # Handles both positive and negative numbers
                push(int(e))
            else:
                n1 = pop()  # Operand 1 (top of the stack)
                n2 = pop()  # Operand 2 (next from the stack)
                if e == "*":
                    res = n2 * n1
                elif e == "+":
                    res = n2 + n1
                elif e == "-":
                    res = n2 - n1
                elif e == "/":
                    res = int(n2 / n1)  # Division truncated towards zero
                push(res)

        return stack[0]  # The result is the only item left in the stack

