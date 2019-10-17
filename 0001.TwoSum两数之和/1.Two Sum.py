"""
以下代码在2019年10月17日在力扣通过执行：
执行用时 :64 ms, 在所有 python3 提交中击败了91.28%的用户
内存消耗 :14.9 MB, 在所有 python3 提交中击败了5.69%的用户
原创作者： JustModesty谦逊
Bilibili：https://www.bilibili.com/video/av71362704/
Youtube：https://www.youtube.com/watch?v=03wdkQsa49c&t=66s
代码存放在Github: https://github.com/JustModesty/Leetcode-Python-Java-Solution
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