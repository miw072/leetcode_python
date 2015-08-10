class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict: return False

        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1, len(s)+1):
        	for j in xrange(i):
        		if dp[j] and s[j:i] in wordDict:
        			dp[i] = True

        return dp[len(s)]			