/*
以下代码在2019年10月16日在力扣通过执行：
执行用时：13 ms, 在所有 java 提交中击败了76.31%的用户
内存消耗 :37.3 MB, 在所有 java 提交中击败了93.56%的用户
原创作者： JustModesty谦逊
视频讲解：
Bilibili：
Youtube：
 */

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
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
         */
        Map<Character, Integer> map = new HashMap<>();
        int start = 0;
        int longestLength =0;
        for (int i=0; i<s.length(); i++){
            if (map.containsKey(s.charAt(i))){
                if (map.get(s.charAt(i))<start){
                    longestLength = Math.max(longestLength, i-start+1);
                }
                else{
                    int preIndex = map.get(s.charAt(i));
                    longestLength = Math.max(longestLength, i-preIndex);
                    start = preIndex + 1;
                }
            }
            else{
               longestLength = Math.max(longestLength, i-start+1);
            }
            map.put(s.charAt(i), i);
        }
        return longestLength;
    }
}