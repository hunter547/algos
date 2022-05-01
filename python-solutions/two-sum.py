from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
      # Declare a hash map that will store already seen values as 
      # the nums array is being iterated through 
      hashmap = {}
      for i in range(len(nums)):
        # Take the difference between target and the number at
        # index i in nums. This difference represents our matching
        # number that will equal the target.
        complement = target - nums[i]
        # if that number has been seen before in our hashmap
        # then we know that the store index value is our match
        # and we can return i and the index of the matched value
        if complement in hashmap:
          return [hashmap[complement], i]
        # If no match has been found, document num and index of
        # the current iteration, as it may be a future match
        # in a subsequent iteration
        hashmap[nums[i]] = i

print(twoSum([2, 3, 5, 8, 4, 6], 10))