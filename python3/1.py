class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited: dict[int, int] = {}
        for i, n in enumerate(nums):
            j = visited.get(target - n)
            if j is not None:
                return [j, i]
            visited[n] = i
        return []
