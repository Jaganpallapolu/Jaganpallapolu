class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_element = stack.pop()
                if current_element == "(":
                    if char != ")":
                        return False
                if current_element == "{":
                    if char != "}":
                        return False
                if current_element == "[":
                    if char != "]":
                        return False
        if stack:
            return False
        else: 
            return True



