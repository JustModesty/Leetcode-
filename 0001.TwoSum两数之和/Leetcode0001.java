/*
以下代码在2019年10月17日通过了执行。
执行用时 :3 ms, 在所有 java 提交中击败了98.91%的用户
内存消耗 :37 MB, 在所有 java 提交中击败了92.71%的用户
原创作者： JustModesty谦逊
Bilibili：https://www.bilibili.com/video/av71362704/
Youtube：https://www.youtube.com/watch?v=03wdkQsa49c&t=66s
代码存放在Github: https://github.com/JustModesty/Leetcode-Python-Java-Solution
 */

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
