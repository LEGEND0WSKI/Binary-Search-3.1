# Time:O(log(n))
# Space:O(1)
# Leetcode: Yes
# Issues: No

# binary search
class Solution:
    def hIndex(self, citations: List[int]): # -> int:
        n = len(citations)
        # underlying assumtion is the array is sorted we can ignore all the terms to the right of mid since they will always true
        low, high = 0,n-1

        while low <= high:
            mid = low + (high-low)//2

            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1

        return n-low


# 2 pointer(logn)
class Solution:
    def hIndex(self, citations: List[int]): # -> int:
        n = len(citations)
        l, r = 0,n-1

        while l <= r:
            h = n - l
            if citations[l] >= h:
                return h
            l +=1
        return 0

#  1 pass(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        r = n - 1  

        while r >= 0:
            h = n - r  
            if citations[r] >= h:  
                r -= 1  
            else:
                return h - 1  
        return n  


# hashset + enumerate 82/83 test cases
# class Solution:
#     def hIndex(self, citations: List[int]): # -> int:
#         n = len(citations)
#         hset = []

#         for i in range(1,n+1):
#             cnt = 0
#             for c in citations:
#                 if c >= i:
#                     cnt +=1
#             hset.append(cnt)
        
#         idx = 0

#         for i,v in enumerate(hset,1):
#             print(v,i)
#             if v >= i:
#                 idx = i
            
#         return idx