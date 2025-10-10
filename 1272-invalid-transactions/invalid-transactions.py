class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transaction_indexes= set()
        transactions_map=defaultdict(list)
        for i, transaction in enumerate(transactions):
            name, time, amount, city= transaction.split(",")
            time= int(time)
            amount= int(amount)
            if amount>1000:
                invalid_transaction_indexes.add(i)
            for prev_time, prev_city, index in transactions_map[name]:
                if prev_city!=city and abs(prev_time-time)<=60:
                    invalid_transaction_indexes.add(i)
                    invalid_transaction_indexes.add(index)
            transactions_map[name].append([time, city, i])
        return [transactions[i] for i in invalid_transaction_indexes]