# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([1,3,5,8,9],8))

# timeComplextiy = o(n^2)

#  def twoSumusingOptimalSolution(nums, target):
   