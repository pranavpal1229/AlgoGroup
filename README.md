Tests Run (in testcases.py): 100%


I am solving question number 1...find duplicate. 

My reasoning for findDuplicate() is I wanted to make the first soltuion run in O(n) time but has O(n) space complexity...however this makes
me create a set which stores all previous numbers. We know that if a number is already in the set...then it has been 
added previously meaning it is the duplicate. 

My reasoning for findDuplicateTwo() is trying to come up with a solution that runs with O(1) space complexity. I was able to do this but had to give up time complexity in this case. For this solution I need through each number (O(n)) but I am also using the .count method on each number which is also O(n). Therefore while the space complexity of O(1), the time complexity is O(n^2).  I probably would not use this solution given the inefficient time complexity. 

In this solution, if a number has a count of more than 1, then we know it is the duplicate and will therefore return the number. 