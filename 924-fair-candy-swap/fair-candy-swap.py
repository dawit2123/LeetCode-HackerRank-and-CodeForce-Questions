class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff= (sum(bobSizes)-sum(aliceSizes))//2
        alice_size_set=set(aliceSizes)
        for target in bobSizes:
            candidate_alice_size= target-diff
            if candidate_alice_size in alice_size_set:
                return [candidate_alice_size, target]