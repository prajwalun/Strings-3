# The calculate method evaluates a basic mathematical expression containing +, -, *, /.

# Use a stack to handle operations and store intermediate results.
# Traverse the string, processing characters:
# - Accumulate digits to form numbers.
# - On encountering an operator or end of string:
#   - Apply the previous operator to the current number and update the stack.
#   - Reset the number and update the previous operator.

# At the end, sum the stack to compute the final result.

# TC: O(n) - Single traversal of the string.
# SC: O(n) - Space for the stack to store intermediate results.


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_operator = '+'
        
        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))
                
                prev_operator = ch
                num = 0
        
        return sum(stack)