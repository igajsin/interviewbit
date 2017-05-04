#!/usr/bin/python3

class Solution(object):
    def maxset(self, A):
        """
        A: list of integers
        return a list of integers
        """
        def split_array(A):
            subarrays = []
            current_subarray = []
            for x in A:
                if x >= 0:
                    current_subarray.append(x)
                elif not current_subarray == []:
                    subarrays.append(current_subarray)
                    current_subarray = []
            subarrays.append(current_subarray)
            return subarrays
        max_sum_subarray = 0
        length_best_subarray = 0
        best_subarray = []
        subarrays = split_array(A)
        for subarray in subarrays:
            sum_subarray = sum(subarray)
            len_subarray = len(subarray)
            if  sum_subarray > max_sum_subarray or \
                (sum_subarray == max_sum_subarray and \
                len_subarray > length_best_subarray):
                best_subarray = subarray
                max_sum_subarray = sum_subarray
                length_best_subarray = len_subarray
        return best_subarray
