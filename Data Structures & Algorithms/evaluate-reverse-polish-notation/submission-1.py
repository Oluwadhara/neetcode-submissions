class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        for char in tokens:
            if char in operators:
                op2 = int(result.pop())
                op1 = int(result.pop())
                oper = operators[char]
                res = operators[char](op1, op2)
                result.append(res)
            else:
                result.append(char)

        return int(result.pop())