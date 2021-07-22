class Solution(object):
    def plusOne(self, digits):
        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits