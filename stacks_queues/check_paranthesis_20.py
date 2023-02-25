# https: // leetcode.com/problems/valid-parentheses/
# Python3 code to Check for
# balanced parentheses in an expression


def check_paranthesis(expression):

    left_chars, LOOKUP = [], {'(' : ')', '{' : '}', '[' : ']'}
    for bracket in expression:
        if bracket in LOOKUP:
            left_chars.append(bracket)
        elif not left_chars or LOOKUP[left_chars.pop()] != bracket:
                return False
    return not left_chars



# Driver code
string = "{[]{()}}"
print(string, "-", check_paranthesis(string))


