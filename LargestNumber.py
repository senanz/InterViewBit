class Greater:
    def __init__(self,x):
        self.x = x
    def __lt__(a, b):
        return a.x + b.x < b.x + a.x
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if all(A):
            str_arr = [x for x in map(str, A)]
            str_arr.sort(key=Greater, reverse=True)
            return ''.join(str_arr)
        else:
            return '0'
