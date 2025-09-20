class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        # 'i' is our closing bracket
        for i in s:
            # It means we have an open bracket
            if i not in hashmap:
                stack.append(i)
            # It means we have a closing bracket
            else:
                if not stack:
                    return False
                else:
                    # Take off the most recent open bracket on the stack
                    popped = stack.pop()
                    if popped != hashmap[i]:
                        return False
        # To make sure we do not have a stack
        return not stack




