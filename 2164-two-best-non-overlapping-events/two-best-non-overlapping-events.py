class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        max_value_from = [0] * n
        max_value_from[-1] = events[-1][2]

        for i in range(n - 2, -1, -1):
            max_value_from[i] = max(max_value_from[i + 1], events[i][2])

        max_sum = 0

        for start, end, value in events:

            left, right = 0, n - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if events[mid][0] > end:  
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            current_sum = value
            if first_true_index != -1:
                current_sum += max_value_from[first_true_index]

            max_sum = max(max_sum, current_sum)

        return max_sum