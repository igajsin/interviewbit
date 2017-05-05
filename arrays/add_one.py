def trnk(L):
    if L == []:
        return []
    elif L[0] == 0:
        return trnk(L[1:])
    else:
        return L

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        B = []
        for i in range(len(A) - 1, -1, -1):
            flag = False
            if A[i] < 9:
                A[i] = A[i] + 1
                break
            else:
                A[i] = 0
                flag = True
        B = A
        if flag:
            B = [1] + B
        B = trnk(B)
        return B
