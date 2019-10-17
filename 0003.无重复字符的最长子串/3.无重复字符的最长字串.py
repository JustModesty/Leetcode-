"""
以下代码在2019年10月16日在力扣通过执行：
执行用时：68 ms, 在所有 python3 提交中击败了95.27%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.01%的用户
原创作者： JustModesty谦逊
视频讲解：
Bilibili：
Youtube：
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        1. 判断是否在字典map里面
        2. 更新longest_length
        3. 更新start （根据情况是否需要）
        4. 更新字典map值
        
        具体步骤：
        每次得到新的字符，进行以下处理
        判断是否在字典map里面：
            True:
                判断之前的字符是否仍在滑动窗口里面（小于start说明不在滑动窗口里面）
                    True：
                        更新规则使用longest_length = max(longest_length, i-start+1)
                    False：
                        获取preIndex
                        更新规则使用longest_length = max(longest_length, i-pre_index)
                        更新start=preIndex+11
            False:
                更新规则使用longest_length = max(longest_length, i-start+1)
        """
        # s非空，最长字串的长度至少为1
        map_char_index = {}
        start = 0
        longest_length = 0
        for i in range(len(s)):
            if s[i] in map_char_index:
                if map_char_index[s[i]] < start:
                    longest_length = max(longest_length, i-start+1)
                else:
                    pre_index = map_char_index[s[i]]
                    longest_length = max(longest_length, i-pre_index)
                    start = pre_index+1
            else:
                longest_length = max(longest_length, i-start+1)
            map_char_index[s[i]] = i
        return longest_length