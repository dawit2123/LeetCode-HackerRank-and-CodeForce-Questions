class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets_count = 0
        array_length = len(arr)
        for first_index in range(array_length):
            for second_index in range(first_index + 1, array_length):
                for third_index in range(second_index + 1, array_length):
                    is_good_triplet = (
                        abs(arr[first_index] - arr[second_index]) <= a and
                        abs(arr[second_index] - arr[third_index]) <= b and
                        abs(arr[first_index] - arr[third_index]) <= c
                    )
                    good_triplets_count += is_good_triplet                  
        return good_triplets_count