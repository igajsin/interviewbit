class Solution(object):
    def wave(self, A):
        B = []
        A.sort()
        for i in range(0, len(A), 2):
            if i + 1 < len(A):
                B.append(A[i+1])
            B.append(A[i])
        return B
