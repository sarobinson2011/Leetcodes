class Solution:
    """ Uses a Hash Map & a Stack """

    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in close_to_open:
                # if the stack is not empty and stack end value is closed by s[i]
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        # if the stack is empty return True
        if not stack:
            return True
        else:
            return False


sol = Solution()
sol.isValid("((])")




