#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        sorted_a, sorted_b = sorted(a), sorted(b)
        m, n = len(sorted_a), len(sorted_b)
        ptr_a, ptr_b = 0, 0
        
        while ptr_a < m and ptr_b < n:
            if sorted_a[ptr_a] < sorted_b[ptr_b]:
                ptr_a += 1
            elif sorted_a[ptr_a] == sorted_b[ptr_b]:
                ptr_b += 1
                ptr_a += 1
            else:
                return False
        return ptr_b == n