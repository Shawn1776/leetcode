class Solution:
    def trap(self, height):
        if height == []: return 0
        max_num = max(height)
        #变量分别表示，最高值下标，返回的面积，从左侧开始的坐标
        max_point, res, start = height.index(max_num), 0, 0
        # 从左侧逼近最高值
        for i in range(1, max_point):
            #左侧值高则可蓄水
            if height[start] > height[i]:
                res += height[start] - height[i]
            #否则更新左侧值
            else:
                start = i
        end = len(height) - 1
        j = end - 1
        # 从右侧逼近最高值，与左侧思路相同
        while j > max_point:
            if height[end] > height[j]:
                res += height[end] - height[j]
            else:
                end = j
            j -= 1
        return res
————————————————
版权声明：本文为CSDN博主「Jiale685」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/L141210113/article/details/88538886
