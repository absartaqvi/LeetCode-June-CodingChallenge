'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which 
randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. 
pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''

class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.array = [0 for _ in range(len(w))]
        self.array[0] = w[0]
        for i in range(1, len(w)):
          self.array[i] = w[i] + self.array[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        x = self.array[-1] * random.random()
        left = 0; right = len(self.array)
        # Traditional Binary Search follows. We can put it in a function of its own.
        while left < right:
          middle = left + (right - left)/2
          if x > self.array[middle]:
            left = middle + 1
          else:
            right = middle
        return left
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

'''
Comments about above solution.
This was a tricky one for me. The epiphany was that "randomness" comes from the weight.
Meaning, the probability that an index - let's say index 4 - will be picked is higher if value
at index 4 is higher. This leads naturally to calculating a prefix sum for the given array.
Now we do a binary search over the given array and find where a "random" value is in that array.
The bit where I stayed stuck for more than an hour was I was using Python's random.randint() with arguments
random.randint(self.array[0], self.array[-1]). This method returns a random integer between the two given values.
Because this value changes on each run, my test cases were not passing.

Eventually, I found random.random() after searching online which gives a "random" float and we then
"spread" it for our distribution (which is self.array) by multiplying with the largest value. Prefix sum
is of course always sorted, so we could just get that by self.array[-1] which is an O(1) operation.
'''
