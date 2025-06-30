from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.num_freq = defaultdict(int)   
        self.freq_count = defaultdict(int) 

    def add(self, number: int) -> None:
        old_freq = self.num_freq[number]
        new_freq = old_freq + 1
        self.num_freq[number] = new_freq

        if old_freq > 0:
            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

        self.freq_count[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if self.num_freq[number] > 0:
            old_freq = self.num_freq[number]
            new_freq = old_freq - 1
            self.num_freq[number] = new_freq

            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]
            
            if new_freq == 0:
                del self.num_freq[number]
            else:
                self.freq_count[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count.get(frequency, 0) > 0