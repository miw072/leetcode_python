class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        wordLength = len(beginWord)
        Q = collections.deque([(beginWord, 1)])
        while Q:
            word, times = Q.popleft()
            for i in xrange(wordLength):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == word[i]: continue
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord == endWord: return times+1
                    if newWord in wordDict:
                        Q.append((newWord, times+1))
                        wordDict.remove(newWord)
        return 0            