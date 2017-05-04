def get_len_greater_than(A, i, x):
    """
    return length of list of element in A, started from A[i] and greater than x
    """
    len_a = len(A)
    while i < len_a:
        if A[i] > x:
            return (len_a - i)
        i += 1
    return 0

class Solution(object):
    def solve(self, A):
        import pdb; pdb.set_trace()
        A.sort()
        for i in range(len(A)):
            if A[i] == get_len_greater_than(A, i, A[i]):
                return 1
        else:
            return -1
