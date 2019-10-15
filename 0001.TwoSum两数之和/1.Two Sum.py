"""
Runtime: 60 ms, faster than 70.15% of Python3 online submissions for Two Sum.
Memory Usage: 15 MB, less than 7.20% of Python3 online submissions for Two Sum
"""
class Solution:
    def twoSum(self, nums, target):
        # key用来存储num值，value用来存储下标index
        hashtable = {}
        for index, num in enumerate(nums):
            # 每次遍历到一个num的时候，enumerate函数可以同时得到它的下标index
            # 去哈希表里面找，有没有target-num这个key，有的话就按顺序先返回对应的下标
            if (target - num) in hashtable:
                return [hashtable[target - num], index]
            else:
                hashtable[num] = index