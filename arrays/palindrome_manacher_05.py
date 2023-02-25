# Python program to implement Manacher's Algorithm 
# http://en.wikipedia.org/wiki/Longest_palindromic_substring

def longestPalindrome(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        # equals to i' = C - (i-C)
        P[i] = (R > i) and min(R - i, P[2*C - i])
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] >= R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


# Driver program 
text1 = "level"
#findLongestPalindromicString(text1) 

temp= longestPalindrome(text1)
print(temp)
   
text2 = "abaaba"
temp  = longestPalindrome(text2) 
print(temp)

text3 = "abababa"
longestPalindrome(text3) 
   
text4 = "abcbabcbabcba"
longestPalindrome(text4) 
   
text5 = "forgeeksskeegfor"
longestPalindrome(text5) 
   
text6 = "caba"
longestPalindrome(text6) 
   
text7 = "abacdfgdcaba"
longestPalindrome(text7) 
   
text8 = "abacdfgdcabba"
longestPalindrome(text8) 
   
text9 = "abacdedcaba"
longestPalindrome(text9) 
