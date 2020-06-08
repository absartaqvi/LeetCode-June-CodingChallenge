'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        array = [0 for _ in range(amount + 1)]
        array[0] = 1
        for x in coins:
          for y in range(1, amount+1):
            if x <= y:
              array[y] = array[y] + array[y-x]
        return array[amount]

'''
Comments on above solution.
It's a standard DP problem. I had understood and solved it way back on algoexpert.io before.
What we are basically doing is calculating how many ways a coin (read how many combinations) of a particular denomination we need to achieve a certain amount. This "certain amount" here is *all* amounts from 0 to target amount in problem.
So consider this:

1. When a "certain amount" is 0 (the inner for loop), how many ways can we achieve it using denomination 1 (which is the first value in `coins` array. Answer is there is 1 way to achieve amount = 0, which is by not using any coins at all.
2. When a "certain amount" is 1 (the inner for loop), how many ways can we achieve it using denomination 1 (which is the first value in `coins` array. Answer is there is 1 way to achieve amount = 1, which is just using that coin.
...
...
...
N. The value at array[y] denotes the ways to achieve amount y using coins of denomination from coints[0..x].
Think of array[y-x] like this: Say x = 2 and y = 2. This means we need to find the number of ways to achieve $2 using a 2-dollar coin. Clearly, the number of ways to do that is just 1 which is to simply use that 2-dollar coin. This 1 comes from array[y-x] => array[2-2] => array[0] => 1.
But we add array[y] to above value because we need the *sum* of combinations/ways from coins encountered in the array so far.

Another variation of the above problem is the LeetCode "Coin Change" problem which asks the *minimum* ways required to achieve given amount. We can simply take the `min` of value at array[y] and array[y-x] in line 45 above and then add 1 to it because we are using current y coin too.
'''
