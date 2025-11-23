# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x

#         left, right = 1, x // 2

#         while left <= right:
#             mid = (left + right) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return right  # right is the integer part of sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        r = x
        while r * r > x:
            r = (r + x // r) // 2

        return r
