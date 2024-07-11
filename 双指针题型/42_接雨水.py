class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        maxn = left[0]
        for i in range(1, len(height)):
            val = height[i]
            maxn = max(maxn, val)
            left[i] = maxn
        maxn = right[-1]
        for i in range(len(height) - 2, -1, -1):
            val = height[i]
            maxn = max(maxn, val)
            right[i] = maxn
        maxn = 0
        for i in range(1, len(left) - 1):
            maxn += min(left[i], right[i]) - height[i]
        return maxn


class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        premax = 0
        endmax = 0
        res = 0
        while l < r:
            premax = max(premax, height[l])
            endmax = max(endmax, height[r])
            if premax < endmax:
                res += premax - height[l]
                l += 1
            else:
                res += endmax - height[r]
                r -= 1
        return res


if __name__ == '__main__':
    height = [int(n) for n in input().split(",")]
    s = Solution2()
    print(s.trap(height))
