from collections import Counter, defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # filter out excessive duplicates from data
        counts = Counter(nums)
        for n in counts:
            counts[n] = min(counts[n], 3 if n == 0 else 2)
        filtered = tuple(sorted(counts.elements()))
        if len(filtered) < 3:
            return []
        # find min and max of data to cut search
        lower_a, lower_b = filtered[0], filtered[1]
        upper_a, upper_b = filtered[-1], filtered[-2]
        # build set of triplets
        triplets: set[tuple[int, int, int]] = set()
        subtotals: dict[int, set[tuple[int, int]]] = defaultdict(set)
        for i, x in enumerate(filtered):
            if -x < lower_a + lower_b:
                break
            if -x in subtotals:
                for z, y in subtotals[-x]:
                    a, b, c = sorted((z, y, x))
                    triplets.add((a, b, c))
            for y in filtered[0:i]:
                subtotals[y + x].add((y, x))
        return list(map(list, triplets))
