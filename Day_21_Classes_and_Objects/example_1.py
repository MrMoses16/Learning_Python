import statistics as stat
import re

# Statistics class
class Statistics():
    def __init__(self, lst):
        self.lst = lst

    def mean(self):
        return stat.mean(self.lst)
    
    def median(self):
        return stat.median(self.lst)
    
    def mode(self):
        return stat.median(self.lst)
    
    def range(self):
        sorted_lst = sorted(self.lst)
        return sorted_lst[-1] - sorted_lst[0]
    
    def var(self):
        return stat.variance(self.lst)
    
    def std(self):
        return stat.stdev(self.lst)
    
    def min(self):
        sorted_lst = sorted(self.lst)
        return sorted_lst[0]
    
    def max(self):
        sorted_lst = sorted(self.lst)
        return sorted_lst[-1]
    
    def count(self):
        return len(self.lst)
    
    def sum(self):
        sum = 0
        for num in self.lst:
            sum += num
        return sum
    
    def freq_dist(self):
        freq = {}
        for num in self.lst:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return freq


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26] 
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range()) 
print('Mean: ', data.mean())
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist()) 
