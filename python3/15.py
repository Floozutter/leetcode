from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: set[tuple[int, int, int]] = set()
        subtotals: dict[int, set[tuple[int, int]]] = defaultdict(set)
        for i, x in enumerate(nums):
            for sub, pairs in subtotals.items():
                if sub + x == 0:
                    for z, y in pairs:
                        a, b, c = sorted((z, y, x))
                        triplets.add((a, b, c))
            for y in nums[0:i]:
                subtotals[y + x].add((y, x))
        return list(map(list, triplets))
