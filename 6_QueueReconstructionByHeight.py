'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        array = []
        for each in people:
          array.insert(each[1], each)
        return array

'''
Comments on above solution.
This one was quite tricky for me. Couldn't solve it without learning more about the possible solutions.
I had reached to the point where my algorithm said: "You can go ahead of me if your height is smaller and
the number of people which are in front of you are less than or equal to mine". But this was not working.

Since I was thinking in the above way, I was not able to successfully solve the problem. A better re-wording of
the algorithm is, at any index we do not care if the current value is smaller. An index only cares if someone with
a greater height has been seen. But a smaller height index cares about how many greater height indices are in front of it.

I am not sure if I can do it any other way besides using the built-in `sorted` method. We first sorted people in descending order by height. So we get this:
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
Now when we insert by index, this means the smallest one will get bubbled to the position equal to its index. And this approach explains I was half way there :) But, half way there is not good enough ;)
'''
