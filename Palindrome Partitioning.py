class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, L):
    	if not s:
    		self.res.append(L)
    		return
    	for i in xrange(1, len(s) + 1):
    		word = s[:i]
    		if word == word[::-1]:
    			self.dfs(s[i:], L + [word])