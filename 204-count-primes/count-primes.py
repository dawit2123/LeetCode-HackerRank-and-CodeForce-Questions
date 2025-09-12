class Solution:
    def countPrimes(self, n: int) -> int:
        # use seive of erastosthenes
        if n<2:
            return 0
        is_prime=[True for _ in range(n)]
        is_prime[0]=is_prime[1]=False
        prime_count=0
        for cur_num in range(2, n):
            if is_prime[cur_num]:
                prime_count+=1
                skip_length=cur_num
                while cur_num+skip_length<n:
                    is_prime[cur_num+skip_length]=False
                    cur_num=cur_num+skip_length
        return prime_count