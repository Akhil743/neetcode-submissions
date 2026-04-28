class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range (0, (len(nums))*2):
            if i<len(nums):
                ans.append(nums[i])
            elif i>=len(nums):
                ans.append(nums[i-len(nums)])
        return ans

        