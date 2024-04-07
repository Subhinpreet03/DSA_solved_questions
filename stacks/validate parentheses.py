"""
Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# code for the above question
def validate_parantheses(s):
    open_paran = ['(', '[', '{']
    close_paran = [')', ']', '}']
    stack_list = []
    for i in range(len(s)):
        if s[i] in open_paran:
            stack_list.append(s[i])
        else:
            if not stack_list:
                return False
            current_char = stack_list.pop()
            if current_char == '{':
                if s[i] != '}':
                    return False
            if current_char == '(':
                if s[i] != ')':
                    return False
            if current_char == '[':
                if s[i] != ']':
                    return False
    if stack_list:
        return False
    return True

if __name__ == '__main__':
    string_list = "{()}[]"
    if validate_parantheses(string_list):
        print('Balanced')
    else:
        print('Not balanced')