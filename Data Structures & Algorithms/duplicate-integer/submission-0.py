class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        res = False

        for num in nums:
            duplicate[num] = duplicate.get(num, 0)+ 1

            if duplicate[num] > 1:
                res = True
        return res
