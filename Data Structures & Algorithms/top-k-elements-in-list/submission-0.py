class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1

        sorted_items = sorted(res.items(), key=lambda item: item[1], reverse=True)

        topk = sorted_items[:k]

        return [item[0] for item in topk]
