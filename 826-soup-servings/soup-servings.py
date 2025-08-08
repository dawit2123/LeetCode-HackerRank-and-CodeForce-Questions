from functools import lru_cache

class Solution:
    def soupServings(self, quantity: int) -> float:
        # Using Least Recently Used (LRU) cache as a decorator to memoize the intermediate results
        @lru_cache(None)
        def recursive_serve(a_quantity: int, b_quantity: int) -> float:
            # Base case: both soups have been served completely or below zero
            if a_quantity <= 0 and b_quantity <= 0:
                return 0.5  # Equal chance of serving A or B completely last

            # Base case: only A has been completely served
            if a_quantity <= 0:
                return 1  # A has been served completely

            # Base case: only B has been completely served
            if b_quantity <= 0:
                return 0  # B has been served completely

            # Recursively calculate the probability of serving A completely first
            # following the four possible operations stated in the problem
            return 0.25 * (
                recursive_serve(a_quantity - 4, b_quantity) +
                recursive_serve(a_quantity - 3, b_quantity - 1) +
                recursive_serve(a_quantity - 2, b_quantity - 2) +
                recursive_serve(a_quantity - 1, b_quantity - 3)
            )

        # An optimization for large n, as the probability tends to 1 when n becomes very large (> 4800)
        if quantity > 4800:
            return 1.0

        # Normalize the soup quantity and cache the calculations to optimize further calls
        # that have reduced soup quantities after servings
        normalized_quantity = (quantity + 24) // 25
        return recursive_serve(normalized_quantity, normalized_quantity)