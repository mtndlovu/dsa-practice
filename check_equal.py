class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        sorted_a, sorted_b = sorted(a), sorted(b)
        for i, n in enumerate(sorted_a):
            if n != sorted_b[i]:
                return False
        return True