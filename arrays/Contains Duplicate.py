# URL: https://leetcode.com/problems/contains-duplicate/


# 217. Contains Duplicate
# Easy

# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Solution:

nums = [1,2,3,1]
uniq_set =  set() # Constant Time
for num in nums:
    if(num in uniq_set):
        return True # The first instance we see a duplicate
    uniq_set.add(num)
return False
    

    # or 

return len(set(nums))!=len(nums)
    # If there are only unique number it should be equal as len(nums)==len(set(nums))
