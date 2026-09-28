class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left+right)//2

            current = 0
            count_days = 1

            for weight in weights:
                if current + weight > mid:
                    count_days += 1
                    current = 0

                current += weight

            if count_days <= days:
                right = mid
            else:
                left = mid + 1

        return left