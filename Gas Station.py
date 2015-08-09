class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        ret, sum, total = 0, 0, 0
        for i in xrange(len(gas)):
        	sum += gas[i] - cose[i]
        	if sum < 0:
        		ret = i + 1
        		sum =0
        	total += gas[i] - cost[i]
        return ret if total >= 0 else -1		