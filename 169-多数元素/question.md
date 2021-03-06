给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
 

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


### 解题思路 
摩尔投票法也叫做同归于尽法，下面举一个三国的例子： 比如有甲、乙、丙三个军队进行厮杀，先假设甲的人数最多，然后发现最后甲和乙的人数全部阵亡，就只剩下丙了，那么这个丙就是人数最多的一个。 摩尔投票法：刚开始有甲乙丙三个候选人，谁都不知道是谁当选，因为票数都是0，先假设数组的甲（这里是数组的第一个元素）为当选人，票数是1，然后遍历整个数组，如果遇到甲的，票数就加一，如果遇到不是甲的，票数就减一，直到甲的票数为0，甲的票数为0就更换候选人，然后继续比较，遍历到数组的最后一个元素就是当选人。然后票数等于0就更换当选人。 我也不知道我举的例子能不能说明白。

正解：这道题的题目是假设数组是存在多数元素的，这个条件非常重要，也就是说这个数组中必定有元素是超过n/2的，也就是说用摩尔投票法找出来的众数一定是超过n/2的

