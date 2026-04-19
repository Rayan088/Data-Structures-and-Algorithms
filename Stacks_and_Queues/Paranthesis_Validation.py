"""
Paranthesis Validation is a problem where you use a stack to check if paranthesis are balanced in a string
A string is valid if an opening paranthesis has a corresponding closing paranthesis and closes in the correct order

The solution entails:
If the current character is an opening paranthesis push it onto the stack
If the character is a closing paranthesis: check if its empty, or pop to the top of the stack and check for corresponding opening paranthesis
Lastly, if the stack if empty, the string is valid.
"""

class Solution:
    def parenthesis_validation(self, s):
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in hashmap: #If char not a closing paranthesis
                stack.append(char)
            else:
                if not stack: #Empty stack
                    return False
                else:
                    popped = stack.pop() #Removes and returns top most element from stack
                    if popped != hashmap[char]: #Checking if closing paranthesis matches opening paranthesis
                        return False
                    
        return not stack #Return true if stack is 
    
#Instances
validator = Solution()

# Valid examples
print(validator.parenthesis_validation("{[]}"))
print(validator.parenthesis_validation("()"))

# Invalid examples
print(validator.parenthesis_validation("({[})"))
print(validator.parenthesis_validation("(]"))