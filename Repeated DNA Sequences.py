class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        lenS = len(s)
        if lenS < 11: 
            return []
        sequenceSet, resultSet, tupleS = set(), set(), tuple(s)
        for i in xrange(lenS - 9):
            slidingWindow = tupleS[i:i+10]
            if slidingWindow in sequenceSet:
                resultSet.add(''.join(slidingWindow))
            else:
                sequenceSet.add(slidingWindow)
        return list(resultSet)