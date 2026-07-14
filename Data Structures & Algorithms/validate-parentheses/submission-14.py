class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { 
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for ch in s:
            if ch not in pairs.keys(): # if opener, push onto stack
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if pairs[ch] != popped:
                    return False
        return len(stack) == 0
