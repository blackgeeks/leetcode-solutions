class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
          middle = (high + low) // 2

          if nums[middle] == target:
              return middle

          if nums[middle] < target:
             low = middle + 1

          if nums[middle] > target:
             high = middle - 0
        return low