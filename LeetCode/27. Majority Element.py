class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Basic Hashmap approch but has O(n) space complexity

        # majority = {}

        # for i in nums:
        #     if not i in majority:
        #         majority[i] = 1
        #     else:
        #         majority[i] += 1
        
        # return max(majority, key = majority.get)

        
        # For O(1) space complexity and in linear time we count the most occuring element if a element occurs it gets count of 1
        # if new element occurs then the value gets decremented and in the case of count = -1 we will change the element to recent (i)

        element = None
        count = 0

        for i in nums:
            if count == 0:
                element = i
            count += (1 if i == element else -1)

        return element
