class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        lenA = len(A)
        ans = 0
        for i in range(1,lenA):
            ans = ans + max(abs(A[i]-A[i-1]),abs(B[i]-B[i-1]))
        return ans
