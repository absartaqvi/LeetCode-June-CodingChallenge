'''
Two City Scheduling

There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 
Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
'''

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # O(nlogn + n) time | O(1) space
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        cost = 0; mid = len(costs)/2
        for i in range(len(costs)):
          if i < mid:
            cost += costs[i][0]
          else:
            cost += costs[i][1]
        return cost
        
'''
Comments about above solution.
The revelation for me was the realization that we cannot change the second index in `costs`.
For A it's always costs[i][0] and for B it's always costs[i][1]. This means some people
have to be sent to city B at higher cost. So all we needed to do is send half the people to city A
at minimum cost. We do this by sorting `costs` by the difference in costs between two cities, then
iterating over the first half of list and sending those half of people to city A. Rest go to city B.
'''
