# Source : https://leetcode.com/problems/two-sum/
# Author : Brandon Taylor
# Date   : 2022-07-03

class Solution:
    def twoSum(self, nums, target):
        newList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i is not j and nums[i]+nums[j] is target:
                    newList.append(i)
                    newList.append(j)
                    return newList

