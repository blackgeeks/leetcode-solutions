class Solution:
    def search(self, nums: [int], target: int) -> int:
        mid = len(nums) //2

        if nums[mid] == target:
            return mid
        # print(nums)
        if len(nums) >1:
            if target >= nums[mid]:
                nums = nums[mid:]
                if self.search(nums,target) != -1:
                    mid = mid + self.search(nums,target)
                else:
                    mid = -1
            elif target < nums[mid]:
                nums = nums[:mid]
                mid = self.search(nums,target)

            return mid
        else:
            return -1
