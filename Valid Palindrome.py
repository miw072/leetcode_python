class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        alpha = []
        for i in xrange(len(s)):
        	if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
        		alpha.append(s[i])
        	elif 'A' <= s[i] <= 'Z':
        		alpha.append(chr(ord(s[i])-ord('A')+ord('a')))
        return alpha == alpha[::-1]			