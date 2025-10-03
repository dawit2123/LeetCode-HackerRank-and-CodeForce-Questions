class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_sets=set()
        transactions_per_name=defaultdict(list)
        for index, transaction in enumerate(transactions):
            name, time, amount, city= transaction.split(",")
            time=int(time)
            amount=int(amount)
            transactions_per_name[name].append([index, time, city])
            if amount>1000:
                invalid_sets.add(index)
            for prev_index, prev_time, prev_city in transactions_per_name[name]:
                if prev_city!=city and abs(prev_time-time)<=60:
                    invalid_sets.add(index)
                    invalid_sets.add(prev_index)
        return [transactions[index] for index in invalid_sets]