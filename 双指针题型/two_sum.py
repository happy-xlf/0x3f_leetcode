from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]


if __name__ == '__main__':
    solution = Solution()
    numbers = [1, 3, 4, 6, 8, 9]
    target = 5
    ans = solution.twoSum(numbers, target)
    print(ans)
