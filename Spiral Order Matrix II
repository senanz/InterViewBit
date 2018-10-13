class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        M = [0] * A
        for i in range(A):
            M[i] = [0] * A
        
        T = 0
        B = A-1
        L = 0
        R = A-1
        dir = 0
        count = 1
        
        while (T<=B and L<=R):
            if dir == 0:
                for i in range(L,R+1):
                    M[T][i] = count
                    count += 1
                T += 1
            elif dir == 1:
                for i in range(T,B+1):
                    M[i][R] = count
                    count += 1
                R -= 1
            elif dir == 2:
                for i in range(R,L-1,-1):
                    M[B][i] = count
                    count += 1
                B -= 1
            elif dir == 3:
                for i in range(B,T-1,-1):
                    M[i][L] = count
                    count += 1
                L += 1
            dir = (dir+1) % A
        return M
