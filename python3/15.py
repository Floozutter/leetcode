from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # filter out excessive duplicates and order
        counts = Counter(nums)
        for n in counts:
            counts[n] = min(counts[n], 3 if n == 0 else 2)
        data = tuple(sorted(counts.elements()))
        if len(data) < 3:
            return []
        # build set of triplets
        triplets: set[tuple[int, int, int]] = set()
        for i, x in enumerate(data):
            visited: set[int] = set()
            lowest = data[0] if i != 0 else data[1]
            for j, y in filter(lambda pair: pair[0] != i, enumerate(data)):
                difference = -x - y
                if difference < lowest:
                    break
                if difference in visited:
                    a, b, c = sorted((x, y, difference))
                    triplets.add((a, b, c))
                visited.add(y)
        return list(map(list, triplets))
