#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param houses int整型一维数组 
# @param heaters int整型一维数组 
# @return int整型
#
from typing import List
# 覆盖房屋的最小加热半径
class Solution:
    def findRadius(self , houses: List[int], heaters: List[int]) -> int:
        # write code here
        houses.sort()
        heaters.sort()
        min_des = []
        for house in houses:
            left = 0
            right = len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            ner_dis = abs(heaters[left] - house)
            if left > 0:
                ner_dis = min(ner_dis, abs(heaters[left - 1] - house))
            min_des.append(ner_dis)
        return max(min_des)
    
s = Solution()
print(s.findRadius([1,2,3,4], [1,4]))
