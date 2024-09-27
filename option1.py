# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    numSet = set()

    for num in input:
        if num not in numSet:
            numSet.add(num)
        else:
            return num

def findDuplicateTwo(input: List[int]) -> int:
    for num in input:
        if input.count(num) > 1:
            return num
        

