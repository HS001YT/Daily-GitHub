class Solution:
    def isValid(self, s: str) -> bool:
        stack = []   # Initialise an empty stack (LIFO)

        for char in s:
            if char in "([{":
                stack.append(char)

            elif char == ")":
                if not stack or stack[-1] != "(":  # not stack works as - stack is empty
                    return False
                stack.pop()

            elif char == "]":
                if not stack or stack[-1] != "[":  # So the condition is - either stack is empty or last bracket is not '['
                    return False
                stack.pop()

            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            else:
                # If any other character is found
                return False  

        return not stack  # True if stack is empty, False otherwise
