class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        n = numerator
        d = denominator
        res = []
        if (n*d < 0):res.append('-')
        n, d = abs(n), abs(d)

        res.append(str(n/d))
        remainder = n%d
        if remainder == 0: return ''.join(res)
        res.append('.')

        remainderPos = {}
        while remainder > 0:
        	if remainder in remainderPos:
        		res.insert(remainderPos[remainder], '(')
        		res.append(')')
        		return ''.join(res)
        	remainderPos[remainder] = len(res)
        	res.append(str(remainder*10/d))
        	remainder = remainder*10%d
        return ''.join(res)		