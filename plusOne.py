class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        lenA = len(A) - 1
        carry = 0
        sum = (A[lenA] + 1) % 10
        carry = (A[lenA] + 1) / 10
        A[lenA] = sum
        for i in range(lenA-1,-1,-1):
            sum = int(A[i] + carry)
            carry = sum // 10
            A[i] = int(sum % 10)
        if carry == 1:
            A.insert(0,int(carry))
        i = 0
        while i < len(A):
            if A[i] == 0:
                A.remove(A[i])
                i = 0
            else:
                break
           
        return A
